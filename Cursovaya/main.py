import eel     #Импорт eel 
from pyowm import OWM     #Импорт модуля pyowm 
from pyowm.utils.config import get_default_config
config_dict = get_default_config()     #Подключение русского языка
config_dict['language'] = "ru"
owm = OWM("a9bfb2a38c47ecf2770bb79a8910ff41", config_dict)    #API ключ по которому происходит передача погоды

@eel.expose    #Декоратор который позволяет передать функцию в JS     
def get_weather(place):    #Функция с передачей параметра
    mgr = owm.weather_manager()    
    observation = mgr.weather_at_place(place)  #Наблюдение погоды в определенном месте, которое укажет пользователь
    w = observation.weather
    w.detailed_status
    w.wind()           #Переменные погодных свойств
    w.rain
    w.clouds 
    humidity = w.humidity
    temp = w.temperature("celsius")["temp"] #Температура в градусах по Цельсию
    
    if temp >= 30:                #Возвращаем погоду в указанном пользователем месте, также я добавил разные приветствия для разных температур!
        return ("На улице реальная жара, одень что-нибудь на голову, а то получишь солнечный удар, ведь там " + str(temp) + "°C, " +     
        "Влажность составляет " + str(humidity) + "%, " + 
        "Скорость ветра " + str(w.wind()["speed"]) + " м/с, сегодня " + str(w.detailed_status) + " и " + str(w.clouds) + "% облачности" )
    if temp >= 27:
        return ("Будь осторожен, солнце - штука опасная, лучше возьми с собой воды, ведь на улице " + str(temp) + "°C, " + 
        "Влажность составляет " + str(humidity) + "%, " + 
        "Скорость ветра " + str(w.wind()["speed"]) + " м/с, сегодня " + str(w.detailed_status) + " и " + str(w.clouds) + "% облачности" )
    if temp >= 25:
        return ("Все еще жарко, может останешься дома? Потому-что на улице " + str(temp) + "°C, " + 
        "Влажность составляет " + str(humidity) + "%, " + 
        "Скорость ветра " + str(w.wind()["speed"]) + " м/с, сегодня " + str(w.detailed_status) + " и " + str(w.clouds) + "% облачности" )
    if temp >= 22:
        return ("Терпимая температура, не забывай про головной убор, ведь на улице " + str(temp) + "°C, " + 
        "Влажность составляет " + str(humidity) + "%, " + 
        "Скорость ветра " + str(w.wind()["speed"]) + " м/с, сегодня " + str(w.detailed_status) + " и " + str(w.clouds) + "% облачности" )
    if temp >= 20:
        return ("Хороший день, как и температура за окном, ведь на улице " + str(temp) + "°C, " + 
        "Влажность составляет " + str(humidity) + "%, " + 
        "Скорость ветра " + str(w.wind()["speed"]) + " м/с, сегодня " + str(w.detailed_status) + " и " + str(w.clouds) + "% облачности" )
    if temp >= 17:
        return ("Господин! На улице замечательная температура, слуги сообщают, что там " + str(temp) + "°C, " + 
        "Влажность составляет " + str(humidity) + "%, " + 
        "Скорость ветра " + str(w.wind()["speed"]) + " м/с, сегодня " + str(w.detailed_status) + " и " + str(w.clouds) + "% облачности" )
    if temp >= 15:
        return ("Прекрасная температура, можно куда-нибудь сходить, ведь за окном " + str(temp) + "°C, " + 
        "Влажность составляет " + str(humidity) + "%, " + 
        "Скорость ветра " + str(w.wind()["speed"]) + " м/с, сегодня " + str(w.detailed_status) + " и " + str(w.clouds) + "% облачности" )
    if temp >= 12:
        return ("Приятный и прохладный ветерок отлично сочитается с вашими планами, ведь за окном " + str(temp) + "°C, " + 
        "Влажность составляет " + str(humidity) + "%, " + 
        "Скорость ветра " + str(w.wind()["speed"]) + " м/с, сегодня " + str(w.detailed_status) + " и " + str(w.clouds) + "% облачности" )
    if temp >= 10:
        return ("И не холодно, и не жарко, лучше не придумаешь, ведь на улице " + str(temp) + "°C, " + 
        "Влажность составляет " + str(humidity) + "%, " + 
        "Скорость ветра " + str(w.wind()["speed"]) + " м/с, сегодня " + str(w.detailed_status) + " и " + str(w.clouds) + "% облачности" )
    if temp >= 7:
        return ("Скоро станет холодно, успейте сходить на прогулку, ведь снаружи " + str(temp) + "°C, " + 
        "Влажность составляет " + str(humidity) + "%, " + 
        "Скорость ветра " + str(w.wind()["speed"]) + " м/с, сегодня " + str(w.detailed_status) + " и " + str(w.clouds) + "% облачности" )
    if temp >= 5:
        return ("Немного похолодало, но еще терпимо, ведь на улице " + str(temp) + "°C, " + 
        "Влажность составляет " + str(humidity) + "%, " + 
        "Скорость ветра " + str(w.wind()["speed"]) + " м/с, сегодня " + str(w.detailed_status) + " и " + str(w.clouds) + "% облачности" )
    if temp >= 3:
        return ("Ученые объявили месяц холода, температура будет понижаться, ведь за окном " + str(temp) + "°C, " + 
        "Влажность составляет " + str(humidity) + "%, " + 
        "Скорость ветра " + str(w.wind()["speed"]) + " м/с, сегодня " + str(w.detailed_status) + " и " + str(w.clouds) + "% облачности" )
    if temp >= 0:
        return ("Даже Король-Лич доволен погодой, ведь на улице " + str(temp) + "°C, " + 
        "Влажность составляет " + str(humidity) + "%, " + 
        "Скорость ветра " + str(w.wind()["speed"]) + " м/с, сегодня " + str(w.detailed_status) + " и " + str(w.clouds) + "% облачности" )
    if temp >= -2:
        return ("Вода уже замерзает, не забудь по-теплее одеться, ведь за окном " + str(temp) + "°C, " + 
        "Влажность составляет " + str(humidity) + "%, " + 
        "Скорость ветра " + str(w.wind()["speed"]) + " м/с, сегодня " + str(w.detailed_status) + " и " + str(w.clouds) + "% облачности" )
    if temp >= -5:
        return ("Выгляни в окно, снег повсюду, ведь на улице " + str(temp) + "°C, " + 
        "Влажность составляет " + str(humidity) + "%, " + 
        "Скорость ветра " + str(w.wind()["speed"]) + " м/с, сегодня " + str(w.detailed_status) + " и " + str(w.clouds) + "% облачности" )
    if temp >= -7:
        return ("Кто-то нарисовал узоры на окне, потому-что на улице " + str(temp) + "°C, " + 
        "Влажность составляет " + str(humidity) + "%, " + 
        "Скорость ветра " + str(w.wind()["speed"]) + " м/с, сегодня " + str(w.detailed_status) + " и " + str(w.clouds) + "% облачности" )
    if temp >= -10:
        return ("Магия льда уже во всю производит снег за окном, ведь на улице " + str(temp) + "°C, " + 
        "Влажность составляет " + str(humidity) + "%, " + 
        "Скорость ветра " + str(w.wind()["speed"]) + " м/с, сегодня " + str(w.detailed_status) + " и " + str(w.clouds) + "% облачности" )
    if temp >= -13:
        return ("Одевайся теплее, уже реально холодно, ведь за окном " + str(temp) + "°C, " + 
        "Влажность составляет " + str(humidity) + "%, " + 
        "Скорость ветра " + str(w.wind()["speed"]) + " м/с, сегодня " + str(w.detailed_status) + " и " + str(w.clouds) + "% облачности" )
    if temp >= -15:
        return ("Вода уже замерзает, не забудь по-теплее одеться, ведь за окном " + str(temp) + "°C, " + 
        "Влажность составляет " + str(humidity) + "%, " + 
        "Скорость ветра " + str(w.wind()["speed"]) + " м/с, сегодня " + str(w.detailed_status) + " и " + str(w.clouds) + "% облачности" )
    if temp >= -18:
        return ("Зима близко, ведь за окном " + str(temp) + "°C, " + 
        "Влажность составляет " + str(humidity) + "%, " + 
        "Скорость ветра " + str(w.wind()["speed"]) + " м/с, сегодня " + str(w.detailed_status) + " и " + str(w.clouds) + "% облачности" )
    if temp >= -20:
        return ("Температура всё падает, когда же это прекратится? На улице " + str(temp) + "°C, " + 
        "Влажность составляет " + str(humidity) + "%, " + 
        "Скорость ветра " + str(w.wind()["speed"]) + " м/с, сегодня " + str(w.detailed_status) + " и " + str(w.clouds) + "% облачности" )
    if temp >= -23:
        return ("Разве может быть так холодно? За окном " + str(temp) + "°C, " + 
        "Влажность составляет " + str(humidity) + "%, " + 
        "Скорость ветра " + str(w.wind()["speed"]) + " м/с, сегодня " + str(w.detailed_status) + " и " + str(w.clouds) + "% облачности" )
    if temp >= -25:
        return ("Шарф и перчатки теперь обычный атрибут любого человека, не забудь их одеть, ведь на улице " + str(temp) + "°C, " + 
        "Влажность составляет " + str(humidity) + "%, " + 
        "Скорость ветра " + str(w.wind()["speed"]) + " м/с, сегодня " + str(w.detailed_status) + " и " + str(w.clouds) + "% облачности" )
    if temp >= -30:
        return ("Наступил ледниковый период, покидать дом не рекомендуется, за стенами убежища " + str(temp) + "°C, " + 
        "Влажность составляет " + str(humidity) + "%, " + 
        "Скорость ветра " + str(w.wind()["speed"]) + " м/с, сегодня " + str(w.detailed_status) + " и " + str(w.clouds) + "% облачности" )
    

        

    return ("В городе " + place + " сейчас " + str(temp) + "°C")

eel.init("web")     #Место где лежит веб-интерфейс программы.
eel.start("index.html", size=(550, 750), mode = "chrome")   #Указываем какой стартовый файл нужно открыть и устанавливаем размер окна веб-приложения
                                                            #Также устанавливаем совместимость для Google Chrome


