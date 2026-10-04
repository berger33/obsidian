---
id: software.seguranca.tranche16.001509
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

# Tuning de Performance e Concorrência no OpenVAS (**`max_hosts`**, **`max_checks`**, **`time_between_request`**) para Não Derrubar Redes ou Alvos Frágeis

## Em uma frase
O que acontece se você disparar uma varredura do OpenVAS contra uma sub-rede `/24` com `max_hosts = 30` e `max_checks = 10` em uma máquina virtual de scanner com apenas 4 GB de RAM, ou contra dispositivos IoT / impressoras / CLPs industriais antigos?

## Por que importa
Dois problemas graves: **(1) Na máquina do scanner**: `30 hosts x 10 NVTs simultâneos = 300 processos/threads de varredura` competindo por CPU e RAM, acionando o **OOM Killer** do Linux que mata o `openvas-scanner` no meio da tarefa; e **(2) Nos alvos da rede**: enviar 10 testes de ataque simultâneos pode travar a pilha TCP/IP de impressoras, câmeras ou sistemas legados!

## Como funciona
Como dimensionar com precisão a concorrência no Target/Task do Greenbone? Ajustando **`Maximum concurrently executed NVTs per host` (`max_checks`, padrão `4`)** e **`Maximum concurrently scanned hosts` (`max_hosts`, padrão `20`)**, além do parâmetro **`time_between_request`** no `openvas.conf` para redes sensíveis!

## Exemplo
```ini
# Exemplo de configuracao controlada em /etc/openvas/openvas.conf para limitar concorrencia de NVTs e proteger redes sensiveis
max_hosts = 10
max_checks = 4
time_between_request = 0
safe_checks = yes
```

## Limites e trade-offs
Olhe a diretiva **`safe_checks = yes`** no `/etc/openvas/openvas.conf` (e nas Scan Configs padrão como `Full and fast`): quando `safe_checks` está ativo (`yes`), o `openvas-scanner` **desabilita todos os scripts NASL classificados nas categorias `ACT_DENIAL`, `ACT_KILL_host`, `ACT_FLOOD` e `ACT_DESTRUCTIVE_ATTACK`** (testes que poderiam causar buffer overflow ou crash em serviços vulneráveis), utilizando apenas testes não-destrutivos!

## Como verificar
Regra prática de dimensionamento de hardware para o container/servidor `openvas-scanner`: reserve aproximadamente **1 vCPU e 1,5 GB de RAM para cada 5 hosts escaneados simultaneamente (`max_hosts`)** com `max_checks = 4`.

## Conexões
- [[openvas-gestao-resultados-qod-quality-of-detection-overrides-false-positives]] — Veja também: Triagem de Resultados no Greenbone: **QoD (*Quality of Detection* — `70%` Default)**, **Notes**, **Overrides** e Filtragem de Falsos Positivos.
- [[openvas-arquitetura-distribuida-scanners-remotos-osp-rust-openvasd]] — Veja também: Arquitetura Distribuída com **Scanners Remotos (`OSP` sobre mTLS)** e o Novo Motor em Rust (**`openvasd`**) em Containers (`ghcr.io/greenbone`).
- [[openvas-arquitetura-greenbone-gvm-gvmd-ospd-openvas-notus-gsa]] — Referência cruzada direta com openvas-arquitetura-greenbone-gvm-gvmd-ospd-openvas-notus-gsa.
- [[openvas-configuracao-alvos-targets-port-lists-alive-test-credenciais]] — Referência cruzada direta com openvas-configuracao-alvos-targets-port-lists-alive-test-credenciais.

## Fontes
- [Greenbone OpenVAS Scanner Official GitHub Repository (`greenbone/openvas-scanner`)](https://raw.githubusercontent.com/greenbone/openvas-scanner/main/README.md) — repositório oficial do motor de varredura OpenVAS e implementação Rust `openvasd` da Greenbone Community Edition; consultado em 2026-10-03.
- [Greenbone Vulnerability Manager (`gvmd`) Official Repository (`greenbone/gvmd`)](https://raw.githubusercontent.com/greenbone/gvmd/main/README.md) — documentação oficial do serviço central `gvmd` cobrindo protocolos GMP e OSP, autenticação JWT, exportação de inteligência e `cve_scan_matching_version`; consultado em 2026-10-03.
