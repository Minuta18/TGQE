function string.starts(String, Start)
    return string.sub(String, 1, string.len(Start))==Start
end
 
function string.split(inputstr, sep)
    if sep == nil then
      sep = "%s"
    end
    local t = {}
    for str in string.gmatch(inputstr, "([^"..sep.."]+)") do
      table.insert(t, str)
    end
    return t
end
  

player_positions = {}
player_quest_started = {}
player_has_key = {}

function reply_with_text(msg, text)
    new_msg = engine.telegram.LuaMessage:create()
    new_msg.chat_id = msg.chat_id
    new_msg.message_text = text

    engine.telegram.send(new_msg)
end

function on_send(msg)
    if string.starts(msg.message_text, "/start") then
        player_quest_started[msg.chat_id] = true
        player_positions[msg.chat_id] = "старт"
        player_has_key[msg.chat_id] = false
        reply_with_text(msg, "Вы очнулись в странной комнате. Перед вами проход на склад и дверь под кодовым замком...")
    end

    if not player_quest_started[msg.chat_id] then
        return
    end

    if string.starts(msg.message_text, "/showmap") then
        if player_positions[msg.chat_id] == "старт" then
            reply_with_text(msg, "(старт) ←→ финиш\n  ↑↓\nсклад")
            return
        elseif player_positions[msg.chat_id] == "финиш" then
            reply_with_text(msg, "старт ←→ (финиш)\n ↑↓\nсклад")
            return
        elseif player_positions[msg.chat_id] == "склад" then
            reply_with_text(msg, "старт ←→ финиш\n ↑↓\n(склад)")
            return
        end
    end

    if string.starts(msg.message_text, "/location") then
        args = string.split(msg.message_text)
        if (table.getn(args) < 2) then
            reply_with_text(msg, "Укажите локацию для перехода")
            return
        end

        if (args[2] == "старт") then
            player_positions[msg.chat_id] = "старт"
            reply_with_text(msg, "Вы перешли на локацию: старт")
            return
        end
        if (args[2] == "склад") then
            player_positions[msg.chat_id] = "склад"
            if not player_has_key[msg.chat_id] then
                reply_with_text(msg, "Вы перешли на локацию: склад\nВы заметили бумажку на полу")
            else
                reply_with_text(msg, "Вы перешли на локацию: склад")
            end
            return
        end
        if (args[2] == "финиш") then
            if player_positions[msg.chat_id] == "склад" then
                reply_with_text(
                    msg, "Вы не можете попасть на эту локацию отсюда"
                )
                return
            end

            if not player_has_key[msg.chat_id] then
                reply_with_text(
                    msg, "Вы не знаете пароль"
                )
                return
            end

            player_positions[msg.chat_id] = "финиш"
            player_quest_started[msg.chat_id] = false
            reply_with_text(
                msg, "Вы прошли квест! Используйте /start чтобы начать сначала"
            )
            return
        end
        reply_with_text(msg, "Такой локации несуществует")
    end

    if string.starts(msg.message_text, "/getitem") then
        if player_positions[msg.chat_id] == "склад" then
            if not player_has_key[msg.chat_id] then
                reply_with_text(msg, "Ва нашли предмет: записка с паролем")
                player_has_key[msg.chat_id] = true
            else
                reply_with_text(msg, "Вы ничего не обнаружили")
            end
        else
            reply_with_text(msg, "Вы ничего не обнаружили")
        end
        return
    end

    if string.starts(msg.message_text, "/help") then
        reply_with_text(msg, "Команды:\n/start - начинает игру\n/showmap - показывает карту\n/location - перейти на локацию\n/getitem - подбирает предмет")
        return
    end
end