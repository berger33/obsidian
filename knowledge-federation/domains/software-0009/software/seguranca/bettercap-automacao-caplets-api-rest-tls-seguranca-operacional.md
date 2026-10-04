---
id: software.seguranca.tranche06.000570
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
fontes: ["https://raw.githubusercontent.com/bettercap/bettercap/master/README.md", "https://raw.githubusercontent.com/bettercap/caplets/master/README.md", "https://www.bettercap.org/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Bettercap: Desenvolvimento de **Caplets (`.cap`)** Auditáveis, Hardening do Módulo `api.rest` e Governança de Escopo em Pentests

## Em uma frase
Escrever **Caplets (`.cap`)** versionados em Git para cada procedimento de teste do Red Team / Pentest garante que os parâmetros de escopo (IPs permitidos, taxas de *throttling*, interfaces e arquivos de saída PCAP/log) sejam revisados antes da execução e que a sessão inteira seja 100% reprodutível.

## Por que importa
Digitar comandos manualmente em tempo real durante uma janela curta de teste em produção aumenta o risco de erros de digitação em máscaras CIDR ou esquecimento de flags de contenção; um arquivo `.cap` documenta exatamente cada comando e timestamp.

## Como funciona
Quando o módulo **`api.rest`** é utilizado para integrar o Bettercap a scripts Python ou à Web UI (`https.server`), ele expõe `/api/session` (estado completo da rede, WiFi, BLE e módulos), `/api/cmd` (execução de comandos) e `/api/events` (WebSocket de eventos em tempo real) protegidos por autenticação HTTP Basic sobre TLS.

## Exemplo
```text
# Exemplo de arquivo audit_scope_vlan20.cap documentado e restrito ao escopo aprovado
set $target_host 10.10.20.55
set net.sniff.output /cases/pentest/vlan20_target55.pcap
set net.sniff.filter "host 10.10.20.55"
net.recon on
net.sniff on
syn.scan $target_host 22,80,443,445,3389
```

## Limites e trade-offs
Ao encerrar qualquer teste ativo de Camada 2 no Bettercap, encerre graciosamente o processo (`q` ou `exit` no console, ou `SIGINT`) para que o Bettercap envie automaticamente os pacotes ARP/NDP de restauração (*re-ARPing*) devolvendo as tabelas ARP dos hosts testados ao estado original.

## Como verificar
Valide em laboratório que após executar `q` no Bettercap a tabela ARP (`arp -a` / `ip neigh`) do host testado aponta novamente para o endereço MAC legítimo do gateway.

## Conexões
- [[bettercap-monitoramento-eventos-events-stream-triggers-webhooks]] — Veja também: Bettercap: Monitoramento de Eventos (`events.stream`), Filtros (`events.ignore`), Gatilhos Reativos (`events.on`) e Sensores de Honeypot L2.
- [[bettercap-arquitetura-modulos-interativos-caplets-api-rest-websocket]] — Referência cruzada direta com bettercap-arquitetura-modulos-interativos-caplets-api-rest-websocket.
- [[bettercap-auditoria-mitm-arp-spoof-ndp-spoof-dhcp6-defesas-l2]] — Referência cruzada direta com bettercap-auditoria-mitm-arp-spoof-ndp-spoof-dhcp6-defesas-l2.
- [[responder-escopo-responder-conf-respondto-dontrespondto-autoignore]] — Referência cruzada direta com responder-escopo-responder-conf-respondto-dontrespondto-autoignore.

## Fontes
- [Bettercap Official GitHub — Network, WiFi, BLE, HID & CAN-bus Framework](https://raw.githubusercontent.com/bettercap/bettercap/master/README.md) — documentação oficial do Bettercap cobrindo arquitetura em Go e módulos de auditoria Ethernet, WiFi, BLE, HID e CAN; consultado em 2026-10-03.
- [Bettercap Caplets Official GitHub — Scripting Interactive Sessions](https://raw.githubusercontent.com/bettercap/caplets/master/README.md) — repositório e documentação oficial de automação de sessões do Bettercap com arquivos .cap (caplets); consultado em 2026-10-03.
- [Bettercap Official Documentation Portal](https://www.bettercap.org/) — documentação oficial do projeto Bettercap; consultado em 2026-10-03.
