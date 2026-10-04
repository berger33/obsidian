---
id: software.seguranca.tranche06.000560
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

# Wireshark & `tshark`: Captura Remota Segura via **Extcap (`sshdump` / `ciscodump`)** e Padronização de *Configuration Profiles* (`-C`) para o SOC

## Em uma frase
A arquitetura **Extcap** do Wireshark permite iniciar capturas de pacotes ao vivo em servidores Linux remotos, roteadores ou containers Kubernetes diretamente da estação local do analista através de um túnel SSH autenticado (**`sshdump`**), sem precisar instalar interfaces gráficas nem copiar arquivos `.pcap` temporários no servidor de produção.

## Por que importa
Evita duas más práticas operacionais comuns durante incidentes: salvar capturas enormes que enchem a partição `/` do servidor de produção, ou esquecer de excluir o filtro da própria conexão SSH do analista (`not port 22`), gerando um loop infinito de tráfego capturando a si mesmo.

## Como funciona
Complementarmente, a flag **`-C <profile_name>`** carrega **Configuration Profiles** padronizados do SOC (contendo colunas customizadas como `JA3`, `SNI`, `Host`, `ServerName`, macros de filtros salvos, chaves de decriptação e regras de coloração para anomalias TCP/TLS/SMB).

## Exemplo
```bash
# Capturar pacotes remotamente via SSH de um servidor de producao (excluindo a propria sessao SSH) direto para o TShark local
ssh secops@10.20.30.40 "tcpdump -U -i eth0 -w - 'not (host 10.99.0.15 and port 22)'" \
  | tshark -r - -n -C soc-dfir-profile -Y "dns or tls.handshake.type == 1"
```

## Limites e trade-offs
Ao usar `sshdump` ou pipe sobre SSH (`tcpdump -U -w -`), inclua **obrigatoriamente** no filtro BPF de captura remota a exclusão do IP/porta da estação do analista (`not (host <ANALYST_IP> and port 22)`), caso contrário cada pacote enviado pelo túnel SSH gerará um novo pacote capturado em realimentação exponencial.

## Como verificar
Exporte o diretório `~/.config/wireshark/profiles/soc-dfir-profile/` para o repositório Git da equipe DFIR para que todos os analistas compartilhem as mesmas colunas e filtros de triagem.

## Conexões
- [[wireshark-dissecadores-customizados-lua-protocolos-c2-proprietarios]] — Veja também: Wireshark & `tshark`: Desenvolvimento de Dissecadores Customizados em **Lua** (`Proto`, `ProtoField`, `DissectorTable`) para Protocolos C2 Proprietários.
- [[wireshark-arquitetura-dissecadores-separacao-privilegios-dumpcap]] — Referência cruzada direta com wireshark-arquitetura-dissecadores-separacao-privilegios-dumpcap.
- [[wireshark-tshark-filtros-captura-bpf-vs-display-filters-duas-passagens]] — Referência cruzada direta com wireshark-tshark-filtros-captura-bpf-vs-display-filters-duas-passagens.
- [[bettercap-arquitetura-modulos-interativos-caplets-api-rest-websocket]] — Referência cruzada direta com bettercap-arquitetura-modulos-interativos-caplets-api-rest-websocket.

## Fontes
- [Wireshark Official GitHub — Architecture & Security Privilege Separation](https://raw.githubusercontent.com/wireshark/wireshark/master/README.md) — documentação oficial do Wireshark cobrindo arquitetura, formato pcapng e isolamento de privilégios no dumpcap; consultado em 2026-10-03.
- [Wireshark Official Manual Page — tshark CLI Reference](https://www.wireshark.org/docs/man-pages/tshark.html) — manual oficial do tshark cobrindo filtros -f vs -Y, análise em duas passagens -2, estatísticas -z e extração -T; consultado em 2026-10-03.
- [Wireshark User's Guide — Official HTML Documentation](https://www.wireshark.org/docs/wsug_html_chunked/) — guia oficial do usuário do Wireshark; consultado em 2026-10-03.
