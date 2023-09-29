# telegram monitor

> Script to monitor F1 Visa slot group

Language: Python

**Description**
Uses telethon module to login as Saurabh Rajguru and read group messages. Refer [[1]][ext1]
Opens video files(as alarms) when new message passes specific filters that could indicate a visa slot being available.

### Requirements

`pip3 install telethon`       #For using telegram API. Refer [[1]][ext1]
api id and hash             #For accessing telegram API
To get id and hash:

1.  Go to <https://my.telegram.org>
2.  Go to application development tools
3.  Fill form (URL to be entered as: www.telegram.org since API is for public telegram not your own implementation of telegram)


## References

[1] <https://github.com/LonamiWebs/Telethon> (telegram;api)
[2] <https://stackoverflow.com/questions/56295761/how-to-get-a-message-from-telegram-groups-by-api> (telegram;api)

[ext1]: https://github.com/LonamiWebs/Telethon (telegram;api)
[ext2]: https://stackoverflow.com/questions/56295761/how-to-get-a-message-from-telegram-groups-by-api (telegram;api)

