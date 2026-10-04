---
id: software.seguranca.tranche16.001503
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-16.md"
fontes: ["https://raw.githubusercontent.com/greenbone/openvas-scanner/main/README.md", "https://raw.githubusercontent.com/greenbone/gvmd/main/README.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Configuração de **Targets, Port Lists e `Alive Test`** no Greenbone/OpenVAS: Evitando Falsos Negativos em Hosts com Firewall que Bloqueia `ICMP Echo`

## Em uma frase
Qual é a causa número 1 de o **OpenVAS / GVM** terminar uma varredura em 10 segundos com **0 vulnerabilidades e 0 hosts encontrados** ao escanear servidores na nuvem (AWS, Azure, GCP) ou atrás de firewalls corporativos?

## Por que importa
É a configuração padrão do **`Alive Test` (*Teste de Host Ativo*)** no objeto **Target**! Por padrão (`Scan Config Default`), o OpenVAS tenta verificar se o IP está vivo enviando um ping **`ICMP Echo Request`** (e probes TCP nos portos 80/443): se o Security Group da AWS ou o firewall do servidor bloquear `ICMP` e o servidor só tiver as portas `2222` e `8443` abertas, o OpenVAS assume que o IP está desligado (*Dead Host*) e **nem sequer inicia a varredura de portas nele**!

## Como funciona
Como resolver isso? Configurando o **`Alive Test` do Target para `Consider Alive`** (para sub-redes onde você já sabe que os IPs existem) ou **`TCP-SYN Service Ping` / `ARP Ping`**, e selecionando a **Port List** adequada (ex.: `All IANA assigned TCP` vs. `All IANA assigned TCP and UDP` vs. `All TCP and Nmap top 100 UDP`)!

## Exemplo
```xml
<!-- Exemplo de comando XML do protocolo GMP (create_target) criando um Target com Alive Test = Consider Alive e Port List IANA TCP -->
<create_target>
  <name>Servidores-Producao-DMZ</name>
  <hosts>192.0.2.10, 192.0.2.20-30</hosts>
  <alive_tests>Consider Alive</alive_tests>
  <port_list id="33d0cd82-57c6-11e1-8ed1-406186ea4fc5"/>
</create_target>
```

## Limites e trade-offs
Veja no XML GMP acima o parâmetro **`<alive_tests>Consider Alive</alive_tests>`**: quando você escaneia uma lista específica de IPs de produção descobertos previamente (por exemplo, exportados do `Subfinder`/`Naabu` ou do inventário da nuvem), definir `Consider Alive` garante que 100% dos hosts sejam escaneados independentemente de regras de bloqueio de ICMP!

## Como verificar
Cuidado apenas para **NÃO usar `Consider Alive` em uma sub-rede `/16` ou `/24` quase vazia**: se você marcar 254 IPs como `Consider Alive` quando apenas 5 existem, o scanner gastará horas esperando timeouts TCP em 249 IPs inexistentes!

## Conexões
- [[openvas-sincronizacao-feeds-greenbone-nvt-scap-cert-gvmd-data]] — Veja também: Sincronização dos Feeds de Inteligência do Greenbone (**`greenbone-feed-sync`**): **NVTs (NASL)**, **SCAP (`CVE` / `CPE`)**, **CERT (`DFN-CERT`)** e **`GVMD_DATA`**.
- [[openvas-varredura-autenticada-ssh-smb-esxi-snmp-notus-scanner]] — Veja também: Varreduras Autenticadas (**Authenticated Scans — SSH, SMB/WMI, ESXi e SNMP**) e o Motor **`notus-scanner`** no Greenbone/OpenVAS.
- [[openvas-arquitetura-greenbone-gvm-gvmd-ospd-openvas-notus-gsa]] — Referência cruzada direta com openvas-arquitetura-greenbone-gvm-gvmd-ospd-openvas-notus-gsa.

## Fontes
- [Greenbone OpenVAS Scanner Official GitHub Repository (`greenbone/openvas-scanner`)](https://raw.githubusercontent.com/greenbone/openvas-scanner/main/README.md) — repositório oficial do motor de varredura OpenVAS e implementação Rust `openvasd` da Greenbone Community Edition; consultado em 2026-10-03.
- [Greenbone Vulnerability Manager (`gvmd`) Official Repository (`greenbone/gvmd`)](https://raw.githubusercontent.com/greenbone/gvmd/main/README.md) — documentação oficial do serviço central `gvmd` cobrindo protocolos GMP e OSP, autenticação JWT, exportação de inteligência e `cve_scan_matching_version`; consultado em 2026-10-03.
