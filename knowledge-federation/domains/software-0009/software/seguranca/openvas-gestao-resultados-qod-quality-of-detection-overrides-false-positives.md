---
id: software.seguranca.tranche16.001508
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

# Triagem de Resultados no Greenbone: **QoD (*Quality of Detection* — `70%` Default)**, **Notes**, **Overrides** e Filtragem de Falsos Positivos

## Em uma frase
Por que, por padrão, a tela de relatórios do Greenbone exibe apenas resultados com **`QoD >= 70%`** e o que significam exatamente os níveis de **QoD (*Quality of Detection*, de `0%` a `100%`)** atribuídos a cada vulnerabilidade detectada?

## Por que importa
O **QoD (*Quality of Detection*)** mede a confiabilidade técnica do método usado pelo NVT para detectar aquela vulnerabilidade: **(1) `100%` (`Exploit` / `Package`)** — o scanner confirmou a falha executando um check direto sem ambiguidade ou verificando o pacote exato via SSH/SMB; **(2) `95%–99%` (`Remote Vuln` / `Registry`)**; **(3) `80%` (`Remote Banner`)** — detecção baseada em versão de banner em sistemas que não fazem backporting (como Windows ou appliances proprietários); e **(4) `30%` (`Remote Banner Unreliable`)** — detecção baseada apenas em banner HTTP/SSH em distribuições Linux como Debian/RHEL/Ubuntu (que fazem backport de patches mantendo o número da versão no banner)!

## Como funciona
Por isso o filtro padrão **`min_qod=70`** é genial: ele **oculta automaticamente os chutes baseados em banners não-confiáveis (`QoD 30%`)**, mantendo a taxa de falsos positivos baixíssima!

## Exemplo
```text
# Exemplo de expressao de filtro de relatorio no Greenbone/GSA para exibir vulnerabilidades Criticas/Altas com QoD >= 70% aplicando Overrides ativos
apply_overrides=1 levels=hml min_qod=70 rows=100 sort-reverse=severity
```

## Limites e trade-offs
E quando uma vulnerabilidade tem `QoD >= 70%`, mas você já aplicou uma mitigação compensatória (ex.: regra de WAF ou bloqueio no firewall) ou confirmou que é um falso positivo naquele host específico? Em vez de ignorar o alerta de cabeça toda semana, crie um **`Override`** no Greenbone vinculado ao `OID` daquele NVT e ao IP do host (com data de expiração opcional!), mudando a severidade para `False Positive` com a justificativa documentada e mantendo `apply_overrides=1` nos relatórios!

## Como verificar
Nas auditorias de servidores Linux onde você não puder usar credenciais SSH, se quiser ver também os alertas de banner para investigação manual, basta reduzir temporariamente o filtro do relatório para `min_qod=30`.

## Conexões
- [[openvas-linguagem-nasl-scripts-nvt-openvas-nasl-execucao-isolada]] — Veja também: Anatomia dos Testes de Vulnerabilidade **NASL (*Network Attack Scripting Language*)** e Execução Isolada de Debug com **`openvas-nasl`**.
- [[openvas-tuning-performance-max-checks-max-hosts-redis-memoria-redes]] — Veja também: Tuning de Performance e Concorrência no OpenVAS (**`max_hosts`**, **`max_checks`**, **`time_between_request`**) para Não Derrubar Redes ou Alvos Frágeis.
- [[openvas-arquitetura-greenbone-gvm-gvmd-ospd-openvas-notus-gsa]] — Referência cruzada direta com openvas-arquitetura-greenbone-gvm-gvmd-ospd-openvas-notus-gsa.
- [[openvas-varredura-autenticada-ssh-smb-esxi-snmp-notus-scanner]] — Referência cruzada direta com openvas-varredura-autenticada-ssh-smb-esxi-snmp-notus-scanner.

## Fontes
- [Greenbone OpenVAS Scanner Official GitHub Repository (`greenbone/openvas-scanner`)](https://raw.githubusercontent.com/greenbone/openvas-scanner/main/README.md) — repositório oficial do motor de varredura OpenVAS e implementação Rust `openvasd` da Greenbone Community Edition; consultado em 2026-10-03.
- [Greenbone Vulnerability Manager (`gvmd`) Official Repository (`greenbone/gvmd`)](https://raw.githubusercontent.com/greenbone/gvmd/main/README.md) — documentação oficial do serviço central `gvmd` cobrindo protocolos GMP e OSP, autenticação JWT, exportação de inteligência e `cve_scan_matching_version`; consultado em 2026-10-03.
