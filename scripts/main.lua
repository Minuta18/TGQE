function dump(o)
    if type(o) == 'table' then
       local s = '{ '
       for k,v in pairs(o) do
          if type(k) ~= 'number' then k = '"'..k..'"' end
          s = s .. '['..k..'] = ' .. dump(v) .. ','
       end
       return s .. '} '
    else
       return tostring(o)
    end
 end
 

function on_send(msg)
    -- print(dump(engine))
    -- print(dump(engine.telegram))
    -- print(dump(engine.telegram.LuaMessage))
    new_msg = engine.telegram.LuaMessage:create()

    new_msg.message_text = string.format(
        "User's text: %s\nGame finished, type /start to continue...",
        msg.message_text
    )
    new_msg.chat_id = msg.chat_id
    engine.telegram.send(new_msg)
end
