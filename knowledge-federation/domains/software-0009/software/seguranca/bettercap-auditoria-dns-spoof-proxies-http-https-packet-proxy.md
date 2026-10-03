---
id: software.seguranca.tranche06.000564
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

# Bettercap: Simulação de Redirecionamento DNS (`dns.spoof`) e Proxies Transparentes Scriptáveis (`http.proxy`, `https.proxy`, `tcp.proxy` e `packet.proxy`)

## Em uma frase
Para validar defesas de aplicação como **DNSSEC**, **DoH/DoT**, **HSTS Preload** (*HTTP Strict Transport Security*) e *Certificate Pinning* em clientes corporativos ou dispositivos IoT, o Bettercap fornece o módulo **`dns.spoof`** e quatro proxies transparentes programáveis em JavaScript (**`http.proxy`**, **`https.proxy`**, **`tcp.proxy`** e **`packet.proxy`**).

## Por que importa
Dispositivos IoT, impressoras multifuncionais e agentes legados frequentemente baixam atualizações de firmware via HTTP puro ou HTTPS sem validar a cadeia de certificação X.509 (`InsecureSkipVerify`); os proxies do Bettercap permitem demonstrar esse risco em laboratório.

## Como funciona
Os módulos `http.proxy` e `tcp.proxy` carregam scripts JavaScript (`set http.proxy.script audit_headers.js`) que expõem os callbacks `onLoad()`, `onRequest(req, res)` e `onResponse(req, res)` (ou `onData(from, to, data)` no `tcp.proxy`), permitindo inspecionar cabeçalhos de segurança ou validar se o cliente aborta imediatamente a conexão TLS quando apresentado a um certificado não confiável.

## Exemplo
```javascript
// Script JavaScript para http.proxy do Bettercap que audita requisicoes HTTP em texto claro de dispositivos IoT
function onLoad() {
    log("Iniciando auditoria passiva de requisicoes HTTP nao-cifradas na VLAN de laboratorio IoT");
}

function onRequest(req, res) {
    log("Alerta HTTP Claro: Host=" + req.Hostname + " Path=" + req.Path + " UA=" + req.GetHeader("User-Agent", ""));
}
```

## Limites e trade-offs
Aplicações web modernas que enviam o cabeçalho `Strict-Transport-Security: max-age=63072000; includeSubDomains; preload` e estão registradas na lista HSTS Preload dos navegadores impedem completamente técnicas legadas de downgrade `sslstrip`.

## Como verificar
Em laboratório de teste IoT, configure `set http.proxy.script audit_headers.js; http.proxy on` e verifique se algum equipamento transmite credenciais ou busca firmware sem TLS.

## Conexões
- [[bettercap-auditoria-mitm-arp-spoof-ndp-spoof-dhcp6-defesas-l2]] — Veja também: Bettercap: Auditoria de Resiliência de Camada 2 contra Spoofing (`arp.spoof`, `ndp.spoof`, `dhcp6.spoof`) e Validação de **DAI / RA Guard**.
- [[bettercap-sniffer-rede-net-sniff-filtros-bpf-expressao-regular]] — Veja também: Bettercap: Captura Seletiva e Inspeção de Tráfego com `net.sniff` (Filtros BPF, Expressões Regulares e Gravação PCAP).
- [[bettercap-arquitetura-modulos-interativos-caplets-api-rest-websocket]] — Referência cruzada direta com bettercap-arquitetura-modulos-interativos-caplets-api-rest-websocket.
- [[wireshark-decriptacao-tls13-sslkeylogfile-dsb-kerberos-keytab]] — Referência cruzada direta com wireshark-decriptacao-tls13-sslkeylogfile-dsb-kerberos-keytab.

## Fontes
- [Bettercap Official GitHub — Network, WiFi, BLE, HID & CAN-bus Framework](https://raw.githubusercontent.com/bettercap/bettercap/master/README.md) — documentação oficial do Bettercap cobrindo arquitetura em Go e módulos de auditoria Ethernet, WiFi, BLE, HID e CAN; consultado em 2026-10-03.
- [Bettercap Caplets Official GitHub — Scripting Interactive Sessions](https://raw.githubusercontent.com/bettercap/caplets/master/README.md) — repositório e documentação oficial de automação de sessões do Bettercap com arquivos .cap (caplets); consultado em 2026-10-03.
- [Bettercap Official Documentation Portal](https://www.bettercap.org/) — documentação oficial do projeto Bettercap; consultado em 2026-10-03.
