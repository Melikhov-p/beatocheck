# beatocheck
Телеграмм бот, для управления каналом-маркетплейсом для музыкантов.  
Возможности:  
 - Принимает заявку на размещение композиции.  
 - Отправляет заявку в чат для модераторов.
 - После одобрения модератерами в чате размещает пост в канале, сообщает пользователю о результате.
 - В случае отклонения заявки автоматически сообщает пользователю о результате.
 - Принимает репорты от пользователей.

Структура:  
 /handlers - папка со всеми хэндлерами  
 /handlers/admins - хендлеры для админов  
 /handlers/admins_chat - хендлеры для чата модераторов  
 /handlers/scripts - сценарии для пользователей (создание заявки на пост)  
 /handlers/users - хендлеры для обычных пользователей  
 
 /keyboards - клавиатуры  
 /config - папка для конфиг файлов (вырезан)
 
