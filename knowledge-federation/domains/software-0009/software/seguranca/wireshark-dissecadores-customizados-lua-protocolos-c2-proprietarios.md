---
id: software.seguranca.tranche06.000559
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-06.md"
fontes: ["https://raw.githubusercontent.com/wireshark/wireshark/master/README.md", "https://www.wireshark.org/docs/man-pages/tshark.html", "https://www.wireshark.org/docs/wsug_html_chunked/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Wireshark & `tshark`: Desenvolvimento de Dissecadores Customizados em **Lua** (`Proto`, `ProtoField`, `DissectorTable`) para Protocolos C2 Proprietários

## Em uma frase
O Wireshark e o `tshark` embarcam um interpretador **Lua** completo (`-X lua_script:meu_dissecador.lua`) que permite escrever dissecadores customizados para protocolos binários internos ou protocolos proprietários de Comando e Controle (C2) de malwares sem precisar recompilar o Wireshark em C.

## Por que importa
Quando a engenharia reversa de um malware no Ghidra/CAPEv2 revela que ele conversa na porta TCP `8443` usando um cabeçalho binário customizado (ex.: 4 bytes de *magic* `0xCAFEBABE`, 1 byte de `opcode`, 4 bytes de `payload_len` e corpo XORed), um script Lua de 30 linhas transforma esses bytes brutos em campos nomeados filtráveis no Wireshark (`my_c2.opcode == 0x04`).

## Como funciona
O script Lua instancia `Proto("c2proto", "Custom Malware C2 Protocol")`, declara os campos com `ProtoField.uint32` / `ProtoField.uint8` / `ProtoField.bytes`, implementa a função `c2proto.dissector(buffer, pinfo, tree)` e registra o protocolo na tabela de portas `DissectorTable.get("tcp.port"):add(8443, c2proto)`.

## Exemplo
```lua
-- Dissecador Lua para protocolo C2 customizado carregavel via: tshark -X lua_script:c2_dissector.lua
local c2_proto = Proto("customc2", "Custom Malware C2 Protocol")
local f_magic  = ProtoField.uint32("customc2.magic", "Magic Header", base.HEX)
local f_opcode = ProtoField.uint8("customc2.opcode", "Command Opcode", base.HEX)
local f_len    = ProtoField.uint32("customc2.length", "Payload Length", base.DEC)
c2_proto.fields = { f_magic, f_opcode, f_len }

function c2_proto.dissector(buffer, pinfo, tree)
    if buffer:len() < 9 or buffer(0,4):uint() ~= 0xCAFEBABE then return 0 end
    pinfo.cols.protocol = "CUSTOM_C2"
    local subtree = tree:add(c2_proto, buffer(), "Custom C2 Frame")
    subtree:add(f_magic, buffer(0,4))
    subtree:add(f_opcode, buffer(4,1))
    subtree:add(f_len, buffer(5,4))
end

DissectorTable.get("tcp.port"):add(8443, c2_proto)
```

## Limites e trade-offs
Se o protocolo C2 aplicar ofuscação simples (como XOR com chave fixa ou RC4 conhecido) sobre o payload, o dissecador Lua pode construir um novo `ByteArray` decodificado e criar uma nova aba de visualização (`ByteArray:tvb("Decrypted Payload")`) diretamente na interface do Wireshark.

## Como verificar
Teste o dissecador via CLI com `tshark -r c2_sample.pcapng -X lua_script:c2_dissector.lua -Y "customc2.opcode == 0x01"`.

## Conexões
- [[wireshark-manipulacao-pcaps-editcap-mergecap-capinfos-reordercap]] — Veja também: Utilitários de Manipulação Forense de PCAPs do Wireshark: `capinfos`, `editcap`, `mergecap` e `reordercap`.
- [[wireshark-captura-remota-sshdump-extcap-perfis-analise-soc]] — Veja também: Wireshark & `tshark`: Captura Remota Segura via **Extcap (`sshdump` / `ciscodump`)** e Padronização de *Configuration Profiles* (`-C`) para o SOC.
- [[wireshark-arquitetura-dissecadores-separacao-privilegios-dumpcap]] — Referência cruzada direta com wireshark-arquitetura-dissecadores-separacao-privilegios-dumpcap.
- [[wireshark-tshark-filtros-captura-bpf-vs-display-filters-duas-passagens]] — Referência cruzada direta com wireshark-tshark-filtros-captura-bpf-vs-display-filters-duas-passagens.

## Fontes
- [Wireshark Official GitHub — Architecture & Security Privilege Separation](https://raw.githubusercontent.com/wireshark/wireshark/master/README.md) — documentação oficial do Wireshark cobrindo arquitetura, formato pcapng e isolamento de privilégios no dumpcap; consultado em 2026-10-03.
- [Wireshark Official Manual Page — tshark CLI Reference](https://www.wireshark.org/docs/man-pages/tshark.html) — manual oficial do tshark cobrindo filtros -f vs -Y, análise em duas passagens -2, estatísticas -z e extração -T; consultado em 2026-10-03.
- [Wireshark User's Guide — Official HTML Documentation](https://www.wireshark.org/docs/wsug_html_chunked/) — guia oficial do usuário do Wireshark; consultado em 2026-10-03.
