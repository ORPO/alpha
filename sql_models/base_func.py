# import configparser
# import re
# import shutil
# import uuid
# import json
#
# import openpyxl
# from lxml import etree
#
# from sql_models.models import *
#
# tables_IO = ['signals_br_mns', 'signals_br_pt', 'signals_br_sar']
# tables_module = ['module_br_mns', 'module_br_pt', 'module_br_sar']
# tables_ss_group = ['ssg_br_mns', 'ssg_br_pt', 'ssg_br_sar']
# tables_service = ['service_signals_br_mns', 'service_signals_br_pt', 'service_signals_br_sar']
# modID_dict = {'IF10X0': 'C3B4', 'IF2181-2': 'C3B3', 'IF10-82-2': '4839', 'DI2377': '7054', 'DI9371': '7061',
#               'AI2437': 'B784', 'AI2237': 'B784', 'BC0083': '7966','BC8083':'7966',
#               'CP3686': 'BF2B', 'CP3586': 'BF2B', 'CS1030': '8144', 'DM9324': '8377', 'DO6322': '7064',
#               'PS9400a': '8076', 'PS3300': '7104', 'AO2437': 'B785'}
#
#
# def create_table(signal, path_base):
#     try:
#         for table in tables_IO:
#             class d_table(IO):
#                 class Meta:
#                     db_table = table
#                     database = SqliteDatabase(path_base + '\mnsbase.db')
#
#             if d_table.table_exists():
#                 signal.emit('Таблица ' + table + ' существует')
#             else:
#                 d_table.create_table()
#                 if d_table.table_exists():
#                     signal.emit('Таблица ' + table + ' создана')
#     except:
#         signal.emit('проверьте путь к базе')
#     try:
#         for table in tables_module:
#             class d_table(module):
#                 class Meta:
#                     db_table = table
#                     database = SqliteDatabase(path_base + '\mnsbase.db')
#
#             if d_table.table_exists():
#                 signal.emit('Таблица ' + table + ' существует')
#             else:
#                 d_table.create_table()
#                 if d_table.table_exists():
#                     signal.emit('Таблица ' + table + ' создана')
#     except:
#         signal.emit('проверьте путь к базе')
#     try:
#         for table in tables_service:
#             class d_table(service_signals):
#                 class Meta:
#                     db_table = table
#                     database = SqliteDatabase(path_base + '\mnsbase.db')
#
#             if d_table.table_exists():
#                 signal.emit('Таблица ' + table + ' существует')
#             else:
#                 d_table.create_table()
#                 if d_table.table_exists():
#                     signal.emit('Таблица ' + table + ' создана')
#     except:
#         signal.emit('проверьте путь к базе')
#
#     try:
#         for table in tables_ss_group:
#             class d_table(ss_group):
#                 class Meta:
#                     db_table = table
#                     database = SqliteDatabase(path_base + '\mnsbase.db')
#
#             if d_table.table_exists():
#                 signal.emit('Таблица ' + table + ' существует')
#             else:
#                 d_table.create_table()
#                 if d_table.table_exists():
#                     signal.emit('Таблица ' + table + ' создана')
#     except:
#         signal.emit('проверьте путь к базе')
#
#
# def read_kzflp(signal, path_base, filename_xls):
#     class signals_app(signals):
#         class Meta:
#             database = SqliteDatabase(path_base + '\mnsbase2.db')
#
#     spisok = []
#
#     try:
#         wb = openpyxl.load_workbook(filename_xls)
#         for sheet in wb.worksheets:
#             if sheet.title.upper() in sheet_name:
#                 print(sheet.title)
#                 rows = sheet.max_row
#                 cols = sheet.max_column
#                 max_rows = 0
#                 for i in range(2, rows + 1):
#                     string = ''
#                     if (sheet.cell(row=i, column=11).value is not None) & (
#                             sheet.cell(row=i, column=3).value is not None):
#                         key = str(sheet.cell(row=i, column=2).value) \
#                               + str(sheet.cell(row=i, column=11).value) \
#                               + str(sheet.cell(row=i, column=12).value) \
#                               + str(sheet.cell(row=i, column=13).value)
#
#                         a_dict = dict(prim_key=key,
#                                       Cabinet=str(sheet.cell(row=i, column=2).value),
#                                       Tagname=str(sheet.cell(row=i, column=3).value),
#                                       Description=str(sheet.cell(row=i, column=4).value),
#                                       KK=str(sheet.cell(row=i, column=5).value),
#                                       Terminalbloc=str(sheet.cell(row=i, column=7).value),
#                                       Contacts=str(sheet.cell(row=i, column=8).value),
#                                       Unit=sheet.cell(row=i, column=11).value,
#                                       Module=sheet.cell(row=i, column=12).value,
#                                       Chanel=sheet.cell(row=i, column=13).value)
#                         spisok.append(a_dict)
#         print(len(spisok))
#         base_wtite_many(signals_app, spisok)
#         signal.emit('Записано')
#     except:
#         signal.emit('Файл КЗФКП не найден')
#
#
# def copy_file(path_file):
#     shutil.copy(path_file, path_file + 'backup')
#
#
# def createConfig(signal, data):
#     config = configparser.ConfigParser()
#     config.add_section("Settings")
#     config.set("Settings", "xls mns path", data[0])
#     config.set("Settings", "xls aspt path", data[1])
#     config.set("Settings", "xls sar path", data[2])
#     config.set("Settings", "OMX AlphaDevstudio", data[3])
#     config.set("Settings", "SQL Base", data[4])
#     config.set("Settings", "XML TagName path", data[5])
#     config.set("Settings", "XML ObjectName path", data[6])
#     config.set("Settings", "XML ColorSheme path", data[7])
#     config.set("Settings", "project name", data[8])
#     config.set("Settings", "XML opc mns", data[9])
#     config.set("Settings", "XML opc aspt", data[10])
#     config.set("Settings", "XML opc sar", data[11])
#     config.set("Settings", "Trend Tree", data[12])
#     try:
#         with open(data[4] + '\config.sav', "w") as config_file:
#             config.write(config_file)
#         signal.emit('Конфиг сохранен')
#     except:
#         signal.emit('Проверьте путь к базе sql. Конфиг сохраняется вместе с базой')
#
#
# def openConfig(signal, cfg, path):
#     try:
#         string_path = str(path).replace('/', '\\')
#         config = configparser.ConfigParser()
#         config.read(string_path)
#         config_data = config.get("Settings", "xls mns path") + "$" \
#                       + config.get("Settings", "xls aspt path") + "$" \
#                       + config.get("Settings", "xls sar path") + "$" \
#                       + config.get("Settings", "OMX AlphaDevstudio") + "$" \
#                       + config.get("Settings", "SQL Base") + "$" \
#                       + config.get("Settings", "XML TagName path") + "$" \
#                       + config.get("Settings", "XML ObjectName path") + "$" \
#                       + config.get("Settings", "XML ColorSheme path") + "$" \
#                       + config.get("Settings", "project name") + "$" \
#                       + config.get("Settings", "XML opc mns") + "$" \
#                       + config.get("Settings", "XML opc aspt") + "$" \
#                       + config.get("Settings", "XML opc sar")+ "$" \
#                       + config.get("Settings", "Trend Tree")
#         cfg.emit(config_data)
#         signal.emit('Конфиг считан')
#     except:
#         signal.emit('Конфиг не считан')
#
#
# def read_br_signal(signal, path_base, filename_xls, type_system):
#     def str_find(str1, arr):
#         for el in arr:
#             if str(str1).find(el) > -1:
#                 return True
#
#     table_sign = 'signals_br' + str(type_system)
#     table_service = 'service_signals_br' + str(type_system)
#     table_module = 'module_br' + str(type_system)
#     table_ssg = 'ssg_br' + str(type_system)
#     db = SqliteDatabase(path_base + '\mnsbase.db')
#
#     class signal_service(service_signals):
#         class Meta:
#             db_table = table_service
#             database = db
#
#     class signals_br(IO):
#         class Meta:
#             db_table = table_sign
#             database = db
#
#     class module_br(module):
#         class Meta:
#             db_table = table_module
#             database = db
#
#     class ssg(ss_group):
#         class Meta:
#             db_table = table_ssg
#             database = db
#
#     spisok = []
#     spisok2 = []
#     try:
#         wb = openpyxl.load_workbook(filename_xls)
#         print(filename_xls)
#         for sheet in wb.worksheets:
#             if sheet.title == "chan":
#                 print(sheet.title)
#                 rows = sheet.max_row
#                 print(rows)
#                 for i in range(2, rows+1):
#                     m_model = str(sheet.cell(row=i, column=7).value).replace('X20', '')
#                     channel = sheet.cell(row=i, column=5).value[-2:]
#                     if m_model[:2] == 'DM':
#                         type = 'DI'
#                         if str(sheet.cell(row=i, column=5).value).find('DigitalOutput') > -1:
#                             channel = str(int(sheet.cell(row=i, column=5).value[-2:]) + 8)
#                             if channel == '9':
#                                 channel = '09'
#                                 print(channel)
#                     else:
#                         type = str(sheet.cell(row=i, column=7).value).replace('X20', '')[:2]
#
#                     a_dict = dict(addr=str(sheet.cell(row=i, column=10).value),
#                                   variable=str(sheet.cell(row=i, column=3).value).replace('_raw',''),
#                                   desc_variable=re.sub(r'\s+', ' ', str(sheet.cell(row=i, column=4).value)),
#                                   channel=str(channel),
#                                   path=str(sheet.cell(row=i, column=6).value),
#                                   m_model=m_model,
#                                   desc_model=str(sheet.cell(row=i, column=9).value),
#                                   hwdesc=str(sheet.cell(row=i, column=8).value),
#                                   position=str(sheet.cell(row=i, column=8).value[-5:]).replace('_', '.'),
#                                   type=type + 's',
#                                   unit=str(sheet.cell(row=i, column=8).value)[:-3],
#                                   addr_channel=str(sheet.cell(row=i, column=8).value) + str(channel))
#                     spisok.append(a_dict)
#             if sheet.title == "slot":
#                 print(sheet.title)
#                 rows = sheet.max_row
#
#                 for i in range(2, rows+1):
#                     a_dict = dict(model=str(sheet.cell(row=i, column=4).value).replace('X20', ''),
#                                   tag=str(sheet.cell(row=i, column=5).value),
#                                   position=str(sheet.cell(row=i, column=8).value),
#                                   type=str(sheet.cell(row=i, column=4).value).replace('X20', '').replace('DM', 'DI')[
#                                        :2])
#                     spisok2.append(a_dict)
#         print(len(spisok))
#         print(len(spisok2))
#         base_wtite_many(signals_br, spisok)
#         base_wtite_many(module_br, spisok2)
#         signal.emit('Записано')
#     except:
#         signal.emit('Файл КЗФКП не найден')
#     try:
#         spisok = []
#         for sig in signals_br.select():
#             if str_find(str(sig.desc_variable).lower(), ['двер', 'переход']):
#                 color_sheme = 4
#             else:
#                 color_sheme = 5
#             if str_find(str(sig.variable), ['CSC']):
#                 addr = str(sig.addr).split(' ')
#                 desc_variable = str(sig.desc_variable).split(' ')
#                 st = ''
#                 for dv in desc_variable:
#                     if str_find(str(dv), ['МНС', 'ПТ', 'САР', 'шкафа']):
#                         dv = ''
#                     st = st + ' ' + dv
#                 a_dict = dict(color_sheme=color_sheme,
#                               addr=addr[0],
#                               variable=str(sig.variable).replace('_raw', ''),
#                               desc_variable=re.sub(r'\s+', ' ', str(st)),
#                               # '.join(str(sig.desc_variable).split(' ')[:-1])),
#                               type=sig.type,
#                               addr_channel=sig.addr_channel,
#                               unit=str(sig.addr_channel)[:-2],
#                               chan=str(sig.addr_channel)[-2:])
#                 spisok.append(a_dict)
#         base_wtite_many(signal_service, spisok)
#         signal.emit('сервисные сигналы сформированы')
#     except:
#         signal.emit('ошибка формирования сервисных сигналов')
#     try:
#         def str_find(str1, str2):
#             if str(str1).find(str2) > -1:
#                 return True
#
#         spisok = []
#         for sig in signal_service.select():
#             a_dict = dict(unit=sig.unit, USO=str(sig.unit)[:-6])
#             spisok.append(a_dict)
#         base_wtite_many(ssg, spisok)
#         signal.emit('групы сервисных сигналов сформированы')
#     except:
#         signal.emit('ошибка формирования групп сервисных сигналов')
#
#
# def add_Ssg(signal, path_base, filename_omx, type_system):
#     table_sign = 'ssg_br' + str(type_system).lower()
#     db = SqliteDatabase(path_base + '\mnsbase.db')
#
#     class ssg(ss_group):
#         class Meta:
#             db_table = table_sign
#             database = db
#
#     # try:
#     #     print(filename_omx)
#     #     parser = etree.XMLParser(remove_blank_text=True)
#     #     tree = etree.parse(filename_omx,parser)
#     #     root = tree.getroot()
#     #     for el in root.iter(omx_xml.dp_application_object):
#     #         if el.attrib['name'] == "Application_PLC" + str(type_system).upper():
#     #             apl = el
#     #     for el1 in apl.iter('{automation.control}object'):
#     #         if el1.attrib['name'] == 'USOs':
#     #             fold = el1
#     #     for obj in ssg.select():
#     #         for el in fold.iter('{automation.control}object'):
#     #             if el.attrib['name'] == obj.USO:
#     #                 print(obj.USO)
#     #                 apl = el
#     #                 name = str(obj.unit)
#     #                 object = etree.Element("{automation.control}object")
#     #                 object.attrib['name'] = name + '_SS'
#     #                 object.attrib['uuid'] = str(uuid.uuid1())
#     #                 object.attrib['base-type'] = "unit._BR_lib.PLC_Types.srv_Signal"
#     #                 object.attrib['aspect'] = "unit._BR_lib.PLC_Types.PLC"
#     #                 apl.append(object)
#     #         tree.write(filename_omx)
#     #         signal.emit('добавлено')
#     # except:
#     #     signal.emit('не добавлено')
#     # #
#     # try:
#     #     tree = etree.parse(filename_omx)
#     #     root = tree.getroot()
#     #     el = ''
#     #     appl = ''
#     #     DIsfolder = ''
#     #     object = ''
#     #     i = 0
#     #     for el in root.iter(omx_xml.dp_application_object):
#     #         if el.attrib['name'] == "Application_PLC" + str(type_system).upper():
#     #             appl = el
#     #     for el1 in appl.iter(omx_xml.ct_object):
#     #         if el1.attrib['name'] == "USOs":
#     #             DIsfolder = el1
#     #     for new_el in DIsfolder.iter(omx_xml.ct_object):
#     #         object = new_el
#     #         query = ssg.select().where(ssg.unit == object.attrib['name'][:-3])
#     #         if query.exists():
#     #             try:
#     #                 obj = ssg.select().where(ssg.unit == object.attrib['name'][:-3]).get()
#     #                 atr1 = etree.Element(omx_xml.init_ref)
#     #                 atr1.attrib['name'] = 'ReferenceInitializer'
#     #                 atr1.attrib['uuid'] = str(uuid.uuid1())
#     #                 atr1.attrib['ref'] = '_mod_DI'
#     #                 atr1.attrib['target'] = 'DIs.' + str(obj.unit)
#     #                 object.append(atr1)
#     #                 i = i + 1
#     #             except:
#     #                 print("не получилось", apl.attrib['name'])
#     #
#     #     tree.write(filename_omx, pretty_print=True)
#     #     signal.emit('добавлены атрибуты')
#     #     print("атрибуты добавлены в", i)
#     # except:
#     #     signal.emit('косяк')
#
#
# def add_MapObjectName(signal, path_base, filename_omx, type_system):
#     table_sign = 'signals_br' + str(type_system)
#     table_service = 'service_signals_br' + str(type_system)
#     table_module = 'module_br' + str(type_system)
#     table_ssg = 'ssg_br' + str(type_system)
#     db = SqliteDatabase(path_base + '\mnsbase.db')
#
#     class signal_service(service_signals):
#         class Meta:
#             db_table = table_service
#             database = db
#
#     class signals_br(IO):
#         class Meta:
#             db_table = table_sign
#             database = db
#
#     class module_br(module):
#         class Meta:
#             db_table = table_module
#             database = db
#
#     class modSc(module):
#         slave = CharField()
#         class Meta:
#             db_table = 'CS_slave' + str(type_system).lower()
#             database = db
#
#     parser = etree.XMLParser(remove_blank_text=True)
#     tree = etree.parse(filename_omx, parser)
#     root = tree.getroot()
#     shutil.copy(filename_omx, filename_omx + '_backup')
#     try:
#         for obj in signals_br.select():
#             type = obj.type[:2]
#             if obj.type[:2] == 'DO': type = 'DI'
#             for elem in root.findall('item'):
#                 parent = elem.getparent()
#                 if (elem.attrib['id'] == "Root" + str(type_system).upper() + "." + obj.type + "." + str(
#                         obj.hwdesc) + ".ch_" + type + "_" + str(obj.channel)):
#                     root.remove(elem)
#             if obj.type in ['AIs', 'DOs', 'DIs']:
#                 apl = root
#                 object = etree.Element('item')
#                 object.attrib['id'] = "Root" + str(type_system).upper() + "." + obj.type + "." + str(
#                     obj.hwdesc) + ".ch_" + type + "_" + str(obj.channel)
#                 object.attrib['value'] = str(obj.desc_variable).replace('None', ' ')
#                 apl.append(object)
#
#         tree.write(filename_omx, pretty_print=True)
#         signal.emit('Создан')
#         for obj in signal_service.select():
#             for elem in root.findall('item'):
#                 parent = elem.getparent()
#                 if (elem.attrib['id'] == "Root" + str(type_system).upper() + ".USOs." + str(obj.unit)[:-6] \
#                         + "." + obj.unit + ".srv_Signal_" + obj.chan + ".ch_DI"):
#                     root.remove(elem)
#             apl = root
#             object = etree.Element('item')
#             object.attrib['id'] = "Root" + str(type_system).upper() + ".USOs." + str(obj.unit)[:-6] \
#                                   + "." + obj.unit + ".srv_Signal_" + obj.chan + ".ch_DI"
#             object.attrib['value'] = str(obj.desc_variable)
#             apl.append(object)
#         tree.write(filename_omx, pretty_print=True)
#         signal.emit('Создан')
#     except:
#         signal.emit('какой то косяк')
#
#     try:
#         query = modSc.select()
#         if query.exists():
#             print('мод цс')
#             for obj in modSc.select():
#                 # for elem in root.findall('item'):
#                 #     # parent = elem.getparent()
#                 #     # if (elem.attrib['id'] == "Root" + str(type_system).upper() + "." + obj.type + "s." + str(obj.hwdesc) + ".ch_" + str(obj.type):
#                 #     #     root.remove(elem)
#                     apl = root
#                     object = etree.Element('item')
#                     object.attrib['id'] = "Root" + str(type_system).upper() + "." + obj.type + "s." + str(
#                         obj.tag) + ".ch_" + obj.type
#                     object.attrib['value'] = obj.slave
#                     apl.append(object)
#
#         tree.write(filename_omx, pretty_print=True)
#         signal.emit('Создан')
#     except:
#         signal.emit('какой то косяк')
#
#
# def add_MapTagName(signal, path_base, filename_omx, type_system):
#     table_sign = 'signals_br' + str(type_system)
#     table_service = 'service_signals_br' + str(type_system)
#     table_module = 'module_br' + str(type_system)
#     table_ssg = 'ssg_br' + str(type_system)
#     db = SqliteDatabase(path_base + '\mnsbase.db')
#
#     class signal_service(service_signals):
#         class Meta:
#             db_table = table_service
#             database = db
#
#     class signals_br(IO):
#         class Meta:
#             db_table = table_sign
#             database = db
#
#     class module_br(module):
#         class Meta:
#             db_table = table_module
#             database = db
#
#     shutil.copy(filename_omx, filename_omx + '_backup')
#     parser = etree.XMLParser(remove_blank_text=True)
#     tree = etree.parse(filename_omx, parser)
#     root = tree.getroot()
#     shutil.copy(filename_omx, filename_omx + '_backup')
#
#     try:
#         signals_br.path = path_base
#         for obj in signals_br.select():
#
#             if obj.type in ['AIs', 'DOs', 'DIs']:
#                 type = obj.type[:2]
#                 if obj.type[:2] == 'DO': type = 'DI'
#                 for elem in root.findall('item'):
#                     parent = elem.getparent()
#                     if (elem.attrib['id'] == "Root" + str(type_system).upper() + "." + obj.type[:2] + "s." + str(
#                             obj.hwdesc) + ".ch_" + type + "_" + str(
#                             obj.channel)):
#                         root.remove(elem)
#
#                 apl = root
#                 object = etree.Element('item')
#                 object.attrib['id'] = "Root" + str(type_system).upper() + "." + obj.type[:2] + "s." + str(
#                     obj.hwdesc) + ".ch_" + type + "_" + str(
#                     obj.channel)
#                 object.attrib['value'] = str(str(obj.variable).replace('_raw', '')).replace('None', ' ')
#                 apl.append(object)
#         for obj in signal_service.select():
#             apl = root
#             object = etree.Element('item')
#             print(obj.variable)
#             object.attrib['id'] = "Root" + str(type_system).upper() + ".USOs." + str(obj.unit)[:-6] \
#                                   + "." + obj.unit + ".srv_Signal_" + obj.chan + ".ch_DI"
#             object.attrib['value'] = str(str(obj.variable).replace('_raw', '')).replace('None', '...')
#             apl.append(object)
#         tree.write(filename_omx, pretty_print=True)
#         signal.emit('Создан')
#
#     except:
#         signal.emit('какой то косяк')
#
#
# def add_MapColorSheme(signal, path_base, filename_omx, type_system):
#     table_sign = 'signals_br' + str(type_system)
#     table_service = 'service_signals_br' + str(type_system)
#     table_module = 'module_br' + str(type_system)
#     table_ssg = 'ssg_br' + str(type_system)
#     db = SqliteDatabase(path_base + '\mnsbase.db')
#
#     class signal_service(service_signals):
#         class Meta:
#             db_table = table_service
#             database = db
#
#     class signals_br(IO):
#         class Meta:
#             db_table = table_sign
#             database = db
#
#     class module_br(module):
#         class Meta:
#             db_table = table_module
#             database = db
#
#     shutil.copy(filename_omx, filename_omx + '_backup')
#     parser = etree.XMLParser(remove_blank_text=True)
#     tree = etree.parse(filename_omx, parser)
#     root = tree.getroot()
#
#     try:
#
#         for obj in signal_service.select():
#             apl = root
#             object = etree.Element('item')
#             print(obj.variable)
#             object.attrib['id'] = "Root" + str(type_system).upper() + ".USOs." + str(obj.unit)[:-6] \
#                                   + "." + obj.unit + ".srv_Signal_" + obj.chan
#             object.attrib['value'] = str(obj.color_sheme)
#             apl.append(object)
#         tree.write(filename_omx, pretty_print=True)
#         signal.emit('Создан')
#
#     except:
#         signal.emit('какой то косяк')
#
#
# def add_mod_obj(signal, path_base, filename_omx, type_system):
#     try:
#         table_sign = 'signals_br' + str(type_system).lower()
#         table_module = 'module_br' + str(type_system).lower()
#         db = SqliteDatabase(path_base + '\mnsbase.db')
#         print(table_sign, table_module, db )
#         class ust_analogs(Model):
#             desc = CharField()
#             tag = CharField(primary_key=True)
#             egu = CharField()
#             LLim = CharField()
#             HLim = CharField()
#             sign = CharField()
#
#             class Meta:
#                 db_table = 'Analogs_attrib' + str(type_system).lower()
#                 database = db
#
#         class signals_br(IO):
#             class Meta:
#                 db_table = table_sign
#                 database = db
#
#         class module_br(module):
#             class Meta:
#                 db_table = table_module
#                 database = db
#
#         parser = etree.XMLParser(remove_blank_text=True)
#         tree = etree.parse(filename_omx, parser)
#         root = tree.getroot()
#         i=0
#         for sign in module_br.select():
#             print(sign.model)
#             modID=modID_dict[sign.model] if str(sign.model) in modID_dict else 'None'
#             print(modID)
#             type = sign.type
#             if sign.model == 'IF10X0': type = 'IF'
#             if sign.model == 'IF2181-2': type = 'IF2'
#             if sign.model == 'IF10-82-2': type = 'IF3'
#             if sign.type == 'AO': type = 'AI'
#             for el in root.iter(omx_xml.dp_application_object):
#                 if el.attrib['name'] == "Application" + str(type_system).upper()+"_ARMs":
#                     apl = el
#             for el in apl.iter('{automation.control}object'):
#                 if el.attrib['name'] == str(sign.type) + 's':
#                     apl = el
#                     for elem in apl.findall(omx_xml.ct_object):
#                         parent = elem.getparent()
#                         if (elem.attrib['name'] == str(sign.tag)):
#                             apl.remove(elem)
#                     #                              print('remove', elem.attrib['name'])
#                     object = etree.Element("{automation.control}object")
#                     object.attrib['name'] = sign.tag
#                     object.attrib['uuid'] = str(uuid.uuid1())
#                     object.attrib['base-type'] = "unit.BR_lib.PLC_Types.mod_" + type
#                     object.attrib['aspect'] = "unit.BR_lib.PLC_Types.PLC"
#                     atr1 = etree.Element("attribute")
#                     atr1.attrib['type'] = "unit.System.Attributes.Description"
#                     atr1.attrib['value'] = str(sign.model).replace('a', '')
#                     object.append(atr1)
#                     atr2 = etree.Element("attribute")
#                     atr2.attrib['type'] = "unit.BR_lib.Attributes.ModPosition"
#                     atr2.attrib['value'] = str(sign.position).replace('BC', '').replace('PS', '')
#                     object.append(atr2)
#                     atr3 = etree.Element("attribute")
#                     atr3.attrib['type'] = "unit.BR_lib.Attributes.ModID"
#                     atr3.attrib['value'] = modID
#                     object.append(atr3)
#                     apl.append(object)
#         tree.write(filename_omx, pretty_print=True)
#         signal.emit('добавлено')
#         print(i)
#
#     except:
#         signal.emit('какой косяк 1')
#     try:
#
#         type = ''
#
#
#         for sign in signals_br.select():
#             type = sign.type
#             if sign.type == 'AIs':
#                 type = 'Analogs'
#                 if sign.variable != 'None' and str(sign.variable).find('rez') == -1:
#                     query_str = str(sign.variable).replace('_raw', '')
#                     query = ust_analogs.select().where(ust_analogs.tag == query_str)
#                     if query.exists():
#                         analog = ust_analogs.select().where(ust_analogs.tag == query_str).get()
#                     for el in root.iter(omx_xml.dp_application_object):
#                         if el.attrib['name'] == "Application" + str(type_system).upper()+"ARMs":
#                             apl = el
#                     for el in apl.iter('{automation.control}object'):
#                         if el.attrib['name'] == type:
#                             apl = el
#                             #print(el.attrib['name'])
#                             for elem in apl.findall(omx_xml.ct_object):
#                                 parent = elem.getparent()
#                                 if (elem.attrib['name'] == str(sign.variable).replace('_raw', '')):
#                                     apl.remove(elem)
#
#                             #                              print('remove', elem.attrib['name'])
#                             object = etree.Element("{automation.control}object")
#                             object.attrib['name'] = str(sign.variable).replace('_raw', '')
#                             object.attrib['uuid'] = str(uuid.uuid1())
#                             object.attrib['base-type'] = "unit.BR_lib.PLC_Types.type_analog"
#                             object.attrib['aspect'] = "unit.BR_lib.PLC_Types.PLC"
#                             atr1 = etree.Element("attribute")
#                             atr1.attrib['type'] = "unit.BR_lib.Attributes.EGU"
#                             atr1.attrib['value'] = analog.egu
#                             object.append(atr1)
#                             atr2 = etree.Element("attribute")
#                             atr2.attrib['type'] = "unit.BR_lib.Attributes.HiLim"
#                             atr2.attrib['value'] = analog.HLim
#                             object.append(atr2)
#                             atr3 = etree.Element("attribute")
#                             atr3.attrib['type'] = "unit.BR_lib.Attributes.LowLim"
#                             atr3.attrib['value'] = analog.LLim
#                             object.append(atr3)
#                             apl.append(object)
#                             atr4 = etree.Element("attribute")
#                             atr4.attrib['type'] = "unit.BR_lib.Attributes.SignalName"
#                             atr4.attrib['value'] = sign.desc_variable
#                             object.append(atr4)
#                             atr5 = etree.Element("attribute")
#                             atr5.attrib['type'] = "unit.BR_lib.Attributes.Sign"
#                             atr5.attrib['value'] = analog.sign
#                             object.append(atr5)
#                             apl.append(object)
#         tree.write(filename_omx, pretty_print=True)
#         signal.emit('добавлено')
#     except:
#         signal.emit('какой косяк')
#
#
# def add_map_opcua(signal, path_base, filename_omx, type_system):
#     table_sign = 'signals_br' + str(type_system)
#     table_service = 'service_signals_br' + str(type_system)
#     table_module = 'module_br' + str(type_system)
#     table_ssg = 'ssg_br' + str(type_system)
#     db = SqliteDatabase(path_base + '\mnsbase.db')
#     mod_type = ['BC0083', 'PS9400a', 'PS3300', 'AI2437', 'DO6322', 'DI9371', 'DM9324', 'DO6322', 'IF10X0', 'IF2181-2',
#                 'IF10-82-2', 'CP3686', 'CP3586', 'AI2237', 'CS1030']
#
#     class signal_service(service_signals):
#         class Meta:
#             db_table = table_service
#             database = db
#
#     class signals_br(IO):
#         class Meta:
#             db_table = table_sign
#             database = db
#
#     class module_br(module):
#         class Meta:
#             db_table = table_module
#             database = db
#
#     parser = etree.XMLParser(remove_blank_text=True)
#     tree = etree.parse(filename_omx, parser)
#     root = tree.getroot()
#     i = 0
#
#     try:
#         # DI
#         for obj in module_br.select():
#
#             if obj.model[:2] in ['DI', 'DM', 'DO','AI']:
#                 if obj.model[:2] == 'DI':
#                     modPack = '_DiPack'
#                     root_system = 'Root' + str(type_system).upper() + '.DIs.'
#                 if obj.model[:2] == 'DO':
#                     modPack = '_DoPack'
#                     root_system = 'Root' + str(type_system).upper() + '.DOs.'
#                 if obj.model[:2] == 'DM':
#                     modPack = '_DmPack'
#                     root_system = 'Root' + str(type_system).upper() + '.DIs.'
#                 if obj.model[:2] == 'AI':
#                     modPack = '_AiPack'
#                     root_system = 'Root' + str(type_system).upper() + '.AIs.'
#
#
#                 for elem in root.findall('nodeId'):
#                     parent = elem.getparent()
#                     if (elem.text.get('nodeId') == 'OPC_' + str(obj.tag) + str(modPack)):
#                         root.remove(parent)
#                 apl = root
#                 object = etree.Element('item')
#                 object.attrib['Binding'] = 'Introduced'
#                 np = etree.Element('node-path')
#                 np.text = root_system + str(obj.tag) + '.State'
#                 object.append(np)
#                 namespace = etree.Element('namespace')
#                 namespace.text = "http://br-automation.com/OpcUa/APROL/pv/"
#                 object.append(namespace)
#                 nodeType = etree.Element('nodeIdType')
#                 nodeType.text = 'String'
#                 object.append(nodeType)
#                 nodeId = etree.Element('nodeId')
#                 nodeId.text = 'OPC_' + str(obj.tag) + modPack
#                 object.append(nodeId)
#                 apl.append(object)
#
#         for obj in module_br.select():  # ревизия
#             root_system = 'Root' + str(type_system).upper() + '.'
#             if obj.model in mod_type:
#                 apl = root
#                 object = etree.Element('item')
#                 object.attrib['Binding'] = 'Introduced'
#                 np = etree.Element('node-path')
#                 type = str(obj.model)[:2]
#                 if str(obj.model)[:2] == 'DM':
#                     type = 'DI'
#                 np.text = root_system + type + 's.' + str(obj.tag) + '.Revision'
#                 object.append(np)
#                 namespace = etree.Element('namespace')
#                 namespace.text = "http://br-automation.com/OpcUa/APROL/pv/"
#                 object.append(namespace)
#                 nodeType = etree.Element('nodeIdType')
#                 nodeType.text = 'String'
#                 object.append(nodeType)
#                 nodeId = etree.Element('nodeId')
#                 nodeId.text = 'OPC_' + str(obj.tag) + '_hwVer'
#                 object.append(nodeId)
#                 apl.append(object)
#         for obj in module_br.select():  # SN
#             root_system = 'Root' + str(type_system).upper() + '.'
#             if obj.model in mod_type:
#                 apl = root
#                 object = etree.Element('item')
#                 object.attrib['Binding'] = 'Introduced'
#                 np = etree.Element('node-path')
#                 type = str(obj.model)[:2]
#                 if str(obj.model)[:2] == 'DM':
#                     type = 'DI'
#                 np.text = root_system + type + 's.' + str(obj.tag) + '.SerialNumber'
#                 object.append(np)
#                 namespace = etree.Element('namespace')
#                 namespace.text = "http://br-automation.com/OpcUa/APROL/pv/"
#                 object.append(namespace)
#                 nodeType = etree.Element('nodeIdType')
#                 nodeType.text = 'String'
#                 object.append(nodeType)
#                 nodeId = etree.Element('nodeId')
#                 nodeId.text = 'OPC_' + str(obj.tag) + '_sn'
#                 object.append(nodeId)
#                 apl.append(object)
#         for obj in module_br.select():  # Firmware
#             root_system = 'Root' + str(type_system).upper() + '.'
#             if obj.model in mod_type:
#                 apl = root
#                 object = etree.Element('item')
#                 object.attrib['Binding'] = 'Introduced'
#                 np = etree.Element('node-path')
#                 type = str(obj.model)[:2]
#                 if str(obj.model)[:2] == 'DM':
#                     type = 'DI'
#                 np.text = root_system + type + 's.' + str(obj.tag) + '.Firmware'
#                 object.append(np)
#                 namespace = etree.Element('namespace')
#                 namespace.text = "http://br-automation.com/OpcUa/APROL/pv/"
#                 object.append(namespace)
#                 nodeType = etree.Element('nodeIdType')
#                 nodeType.text = 'String'
#                 object.append(nodeType)
#                 nodeId = etree.Element('nodeId')
#                 nodeId.text = 'OPC_' + str(obj.tag) + '_fwVer'
#                 object.append(nodeId)
#                 apl.append(object)
#
#         for obj in signals_br.select():
#             if obj.type == 'AIs':
#                 apl = root
#                 object = etree.Element('item')
#                 object.attrib['Binding'] = 'Introduced'
#                 np = etree.Element('node-path')
#                 root_system = 'Root' + str(type_system).upper() + '.'
#                 np.text = root_system + 'AIs.' + str(obj.hwdesc) + '.ch' + str(obj.channel) + '_Value'
#                 object.append(np)
#                 namespace = etree.Element('namespace')
#                 namespace.text = "http://br-automation.com/OpcUa/APROL/pv/"
#                 object.append(namespace)
#                 nodeType = etree.Element('nodeIdType')
#                 nodeType.text = 'String'
#                 object.append(nodeType)
#                 nodeId = etree.Element('nodeId')
#                 nodeId.text = 'OPC_' + str(obj.variable)
#                 object.append(nodeId)
#                 apl.append(object)
#
#         for obj in signals_br.select():
#             if obj.type == 'AIs':
#                 if obj.variable != 'None' and str(obj.variable).find('rez') == -1:
#                     apl = root
#                     object = etree.Element('item')
#                     object.attrib['Binding'] = 'Introduced'
#                     np = etree.Element('node-path')
#                     root_system = 'Root' + str(type_system).upper() + '.'
#                     np.text = root_system+'Analogs.' + str(obj.variable).replace('_raw', '') + '.Value'
#                     object.append(np)
#                     namespace = etree.Element('namespace')
#                     namespace.text = "http://br-automation.com/OpcUa/APROL/pv/"
#                     object.append(namespace)
#                     nodeType = etree.Element('nodeIdType')
#                     nodeType.text = 'String'
#                     object.append(nodeType)
#                     nodeId = etree.Element('nodeId')
#                     nodeId.text = 'OPC_' + str(obj.variable).replace('_raw', '')
#                     object.append(nodeId)
#                     apl.append(object)
#
#                     apl = root
#                     object = etree.Element('item')
#                     object.attrib['Binding'] = 'Introduced'
#                     np = etree.Element('node-path')
#                     root_system = 'Root' + str(type_system).upper() + '.'
#                     np.text = root_system+'Analogs.' + str(obj.variable).replace('_raw', '') + '.State'
#                     object.append(np)
#                     namespace = etree.Element('namespace')
#                     namespace.text = "http://br-automation.com/OpcUa/APROL/pv/"
#                     object.append(namespace)
#                     nodeType = etree.Element('nodeIdType')
#                     nodeType.text = 'String'
#                     object.append(nodeType)
#                     nodeId = etree.Element('nodeId')
#                     nodeId.text = 'OPC_' + str(obj.variable).replace('_raw', '') + '_status'
#                     object.append(nodeId)
#                     apl.append(object)
#
#         for obj in module_br.select():
#             if obj.type == 'BC':
#                 apl = root
#                 object = etree.Element('item')
#                 object.attrib['Binding'] = 'Introduced'
#                 np = etree.Element('node-path')
#                 root_system = 'Root' + str(type_system).upper() + '.'
#                 np.text =  root_system + 'BCs.' + obj.tag + '.State'
#                 object.append(np)
#                 namespace = etree.Element('namespace')
#                 namespace.text = "http://br-automation.com/OpcUa/APROL/pv/"
#                 object.append(namespace)
#                 nodeType = etree.Element('nodeIdType')
#                 nodeType.text = 'String'
#                 object.append(nodeType)
#                 nodeId = etree.Element('nodeId')
#                 nodeId.text = 'OPC_' + obj.tag + '_BcPack'
#                 object.append(nodeId)
#                 apl.append(object)
#
#                 apl = root
#                 object = etree.Element('item')
#                 object.attrib['Binding'] = 'Introduced'
#                 np = etree.Element('node-path')
#                 root_system = 'Root' + str(type_system).upper() + '.'
#                 np.text =  root_system + 'BCs.' + obj.tag + '.Losses_IF01'
#                 object.append(np)
#                 namespace = etree.Element('namespace')
#                 namespace.text = "http://br-automation.com/OpcUa/APROL/pv/"
#                 object.append(namespace)
#                 nodeType = etree.Element('nodeIdType')
#                 nodeType.text = 'String'
#                 object.append(nodeType)
#                 nodeId = etree.Element('nodeId')
#                 nodeId.text = 'OPC_' + obj.tag + '_Link1_Loss'
#                 object.append(nodeId)
#                 apl.append(object)
#
#                 apl = root
#                 object = etree.Element('item')
#                 object.attrib['Binding'] = 'Introduced'
#                 np = etree.Element('node-path')
#                 root_system = 'Root' + str(type_system).upper() + '.'
#                 np.text =  root_system + 'BCs.' + obj.tag + '.Losses_IF02'
#                 object.append(np)
#                 namespace = etree.Element('namespace')
#                 namespace.text = "http://br-automation.com/OpcUa/APROL/pv/"
#                 object.append(namespace)
#                 nodeType = etree.Element('nodeIdType')
#                 nodeType.text = 'String'
#                 object.append(nodeType)
#                 nodeId = etree.Element('nodeId')
#                 nodeId.text = 'OPC_' + obj.tag + '_Link2_Loss'
#                 object.append(nodeId)
#                 apl.append(object)
#
#         for obj in module_br.select():
#             if obj.type == 'PS':
#                 apl = root
#                 object = etree.Element('item')
#                 object.attrib['Binding'] = 'Introduced'
#                 np = etree.Element('node-path')
#                 root_system = 'Root' + str(type_system).upper() + '.'
#                 np.text =  root_system + 'PSs.' + obj.tag + '.State'
#                 object.append(np)
#                 namespace = etree.Element('namespace')
#                 namespace.text = "http://br-automation.com/OpcUa/APROL/pv/"
#                 object.append(namespace)
#                 nodeType = etree.Element('nodeIdType')
#                 nodeType.text = 'String'
#                 object.append(nodeType)
#                 nodeId = etree.Element('nodeId')
#                 nodeId.text = 'OPC_' + obj.tag + '_PsPack'
#                 object.append(nodeId)
#                 apl.append(object)
#
#                 apl = root
#                 object = etree.Element('item')
#                 object.attrib['Binding'] = 'Introduced'
#                 np = etree.Element('node-path')
#                 root_system = 'Root' + str(type_system).upper() + '.'
#                 np.text =  root_system + 'PSs.' + obj.tag + '.Voltage'
#                 object.append(np)
#                 namespace = etree.Element('namespace')
#                 namespace.text = "http://br-automation.com/OpcUa/APROL/pv/"
#                 object.append(namespace)
#                 nodeType = etree.Element('nodeIdType')
#                 nodeType.text = 'String'
#                 object.append(nodeType)
#                 nodeId = etree.Element('nodeId')
#                 nodeId.text = 'OPC_' + obj.tag + '_Volt'
#                 object.append(nodeId)
#                 apl.append(object)
#
#         for obj in module_br.select():
#             if obj.type == 'CS':
#                 apl = root
#                 object = etree.Element('item')
#                 object.attrib['Binding'] = 'Introduced'
#                 np = etree.Element('node-path')
#                 root_system = 'Root' + str(type_system).upper() + '.'
#                 np.text =  root_system + 'CSs.' + obj.tag + '.State'
#                 object.append(np)
#                 namespace = etree.Element('namespace')
#                 namespace.text = "http://br-automation.com/OpcUa/APROL/pv/"
#                 object.append(namespace)
#                 nodeType = etree.Element('nodeIdType')
#                 nodeType.text = 'String'
#                 object.append(nodeType)
#                 nodeId = etree.Element('nodeId')
#                 nodeId.text = 'OPC_' + obj.tag + '_CsPack'
#                 object.append(nodeId)
#                 apl.append(object)
#
#                 # apl = root
#                 # object = etree.Element('item')
#                 # object.attrib['Binding'] = 'Introduced'
#                 # np = etree.Element('node-path')
#                 # root_system = 'Root' + str(type_system).upper() + '.'
#                 # np.text =  root_system + 'CSs.' + obj.tag + '.Voltage'
#                 # object.append(np)
#                 # namespace = etree.Element('namespace')
#                 # namespace.text = "http://br-automation.com/OpcUa/APROL/pv/"
#                 # object.append(namespace)
#                 # nodeType = etree.Element('nodeIdType')
#                 # nodeType.text = 'String'
#                 # object.append(nodeType)
#                 # nodeId = etree.Element('nodeId')
#                 # nodeId.text = 'OPC_' + obj.tag + '_Volt'
#                 # object.append(nodeId)
#                 # apl.append(object)
#         for obj in module_br.select():
#             if obj.type == 'IF':
#                 if str(obj.position)[1] == "1": nplc = "Pri"
#                 if str(obj.position)[1] == "2": nplc = "Sec"
#                 if str(obj.position)[1] == "5": nplc = "KS1"
#                 if str(obj.position)[1] == "6": nplc = "KS2"
#                 apl = root
#                 object = etree.Element('item')
#                 object.attrib['Binding'] = 'Introduced'
#                 np = etree.Element('node-path')
#                 root_system = 'Root' + str(type_system).upper() + '.'
#                 np.text =  root_system + 'IFs.' + obj.tag + '.State'
#                 object.append(np)
#                 namespace = etree.Element('namespace')
#                 namespace.text = "http://br-automation.com/OpcUa/APROL/pv/"
#                 object.append(namespace)
#                 nodeType = etree.Element('nodeIdType')
#                 nodeType.text = 'String'
#                 object.append(nodeType)
#                 nodeId = etree.Element('nodeId')
#                 nodeId.text = "OPC_PLC_DMZDiag_"+ nplc +"_SS"+str(obj.position)[4:]
#                 object.append(nodeId)
#                 apl.append(object)
#
#
#
#         tree.write(filename_omx, pretty_print=True)
#
#         signal.emit('Создан')
#     except:
#         signal.emit('какой то косяк')
#
# def trends_tree(signal, path_base, filename_omx):
#     table_trends = ['Analogs_attrib_mns', 'Analogs_attrib_sar','Analogs_attrib_pt']#, 'Analogs_attrib_pt'
#     db = SqliteDatabase(path_base+ '\mnsbase.db')
#     try:
#         class ust_analogs(Model):
#             desc = CharField()
#             tag = CharField(primary_key=True)
#             egu = CharField()
#             LLim = CharField()
#             HLim = CharField()
#             sign = CharField()
#
#             class Meta:
#                 database = db
#
#         data = {}
#         trend = {}
#         trend["UserTree"] = []
#         for table in table_trends:
#             class trends(ust_analogs):
#                 class Meta:
#                     db_table = table
#
#             query = trends.select()
#             if query.exists():
#                 for sign in trends.select():
#                     group = 'Простые аналоги/'
#                     if str(sign.desc).lower().find('темп') > -1: group = 'Температуры/'
#                     if str(sign.desc).lower().find('вибр') > -1: group = 'Вибрации/'
#                     if str(sign.desc).lower().find('смещ') > -1: group = 'Вибрации/'
#                     if str(sign.desc).lower().find('давл') > -1: group = 'Давления/'
#                     if str(sign.tag).find('rez') > -1: group = 'Резерв/'
#                     if table == 'Analogs_attrib_mns':
#                         system = "МНС Каштан/"
#                         root = "MNS"
#                     if table == 'Analogs_attrib_pt':
#                         system = "АСПТ Каштан/"
#                         root = "PT"
#                     if table == 'Analogs_attrib_sar':
#                         system = "САР Каштан/"
#                         root = "SAR"
#                     trend["UserTree"].append({"Signal": {"UserTree": system + group,
#                                                          "OpcTag": "Root_" +root+".Analogs." + sign.tag + ".AIVisualValue",
#                                                          "EUnit": sign.egu,"Description": sign.desc}})
#         wb = openpyxl.load_workbook("E:\Каштан\Trands_SNMP_v2.xlsx")
#         for sheet in wb.worksheets:
#             if sheet.title == "snmp":
#                 print(sheet.title)
#                 rows = sheet.max_row
#                 print(rows)
#         for i in range(2, rows + 1):
#             trend["UserTree"].append({"Signal": {"UserTree": sheet.cell(row=i,column=3).value+"/",
#                                                  "OpcTag": sheet.cell(row=i,column=6).value,
#                                                  "EUnit": sheet.cell(row=i,column=5).value, "Description": sheet.cell(row=i,column=4).value}})
#
#         with open(filename_omx, 'w', encoding='utf-8') as outfile:
#             json.dump(trend, outfile, ensure_ascii=False, indent=4)
#     except:
#         print("не получилось")
#
