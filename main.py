

import pywhatkit
Message = 'היי בובה:]]\n זאת הודעה בעברית'
wait_time_for_writing_msg_in_chrome = 10
wait_time_to_close_tab = 2
phone_num = '+972585845386'
# pywhatkit.sendwhatmsg_instantly(phone_no=phone_num,
#                                 message=Message,
#                                 wait_time=wait_time_for_writing_msg_in_chrome,
#                                 tab_close=True,
#                                 close_time=wait_time_to_close_tab)

save_the_date_img_path = 'save_the_date.jpg'
pywhatkit.sendwhats_image(receiver='Koala',
                          img_path='save_the_date_img_path',
                          caption=Message,
                          wait_time=wait_time_for_writing_msg_in_chrome,
                          tab_close=True,
                          close_time=wait_time_to_close_tab)


