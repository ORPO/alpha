import streamlit as st
import psutil
from peewee import *
import markdown
import time
db = PostgresqlDatabase('postgres', user='postgres', password='postgres',
                        host='127.0.0.1', port=5432)
class Basemodel(Model):  # базовый клас
    class Meta:
        database = db  # модель будет использовать базу данных указанную выше
        shema = 'alpha'

class kzfkp(Basemodel):
    CabinetName = CharField()
    Tag = CharField(null=True)
    SignalName = CharField(null=True)
    Sheme = CharField(null=True)
    TerminalBlock = CharField(null=True)
    Unit = IntegerField(null=True)
    HWDesc = CharField(null=True)
    CabinetTag = CharField(null=True)
    Module = IntegerField(null=True)
    Channel = IntegerField(null=True)
    TypeSignal = CharField(null=True)
    Signal_id = CharField(primary_key=True)
    TypeSheme = CharField(null=True)
    Ttips = CharField(null=True)

class TypeSheme(Basemodel):
    Sheme_id = CharField(primary_key=True)
    TypeObj = CharField()
    Description = CharField(null=True)

qr= kzfkp.select(kzfkp, TypeSheme).join(TypeSheme, on=(TypeSheme.TypeObj == "ZD")).where(
        kzfkp.TypeSheme == TypeSheme.Sheme_id)



x = st.slider('x')
st.write(x, 'squared is', x * x)
st.header('Header')
st.write("""
# Мой веб сервер
>новая строка
"""
         )

with st.form(key='my form'):
    text_input = st.write(label='Вывести КЗФКП')
    submit_button = st.form_submit_button(label='Вывести КЗФКП')
    st.checkbox('Check me out')
    st.text(psutil.cpu_percent())
    st.text("Память всего: {0}, занято: {1} %".format(psutil.virtual_memory()[0], psutil.virtual_memory()[2]))


if submit_button:
   st.table(qr)


st.video('C:\\Users\\chern\\Downloads\\Новогодний корпоратив.mp4')
st.selectbox('Select', [1,2,3])





def clear():
    print("1")
def label1():
# Forms can be declared using the 'with' syntax
    st.header('Header')
    st.title('Заголовок')
    st.write("""
    Мой веб сервер
    """
             )

    st.text(psutil.cpu_percent())
    st.text("Память всего: {0}, занято: {1} %".format(psutil.virtual_memory()[0], psutil.virtual_memory()[2]))

progress_bar = st.progress(0)
status_text = st.empty()
chart = st.line_chart(np.random.randn(10, 2))

for i in range(100):
    # Update progress bar.
    progress_bar.progress(i + 1)

    new_rows = np.random.randn(10, 2)

    # Update status text.
    status_text.text(
        'The latest random number is: %s' % new_rows[-1, 1])

    # Append data to the chart.
    chart.add_rows(new_rows)

    # Pretend we're doing some computation that takes time.
    time.sleep(0.1)

status_text.text('Done!')
st.balloons()