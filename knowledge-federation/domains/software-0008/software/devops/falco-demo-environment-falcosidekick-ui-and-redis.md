---
id: software.devops.tranche03.000246
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-03.md"
fontes: ["https://raw.githubusercontent.com/falcosecurity/falco/master/README.md", "https://github.com/falcosecurity/falco"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Ambiente de demonstração com Docker Compose: Falco, Falcosidekick, Falcosidekick-UI e Redis

## Em uma frase
A subseção `Demo Environment` do README informa que o repositório disponibiliza em `docker/docker-compose/` um ambiente completo de demonstração via Docker Compose que pode ser iniciado em um host Docker e inclui quatro componentes integrados: `falco`, `falcosidekick`, `falcosidekick-ui` e seu banco de dados `redis` requerido.

## Por que importa
Na arquitetura do ecossistema Falco, o `falcosidekick` atua como o hub de encaminhamento que recebe os eventos do Falco e os distribui para dezenas de destinos (Slack, Alertmanager, Loki, SIEMs) além de alimentar a interface web `falcosidekick-ui` apoiada pelo `redis`.

## Como funciona
Utilize a pilha de `docker/docker-compose/` em um host de laboratório para experimentar novas regras de detecção e visualizar imediatamente os alertas disparados na interface `falcosidekick-ui`.

## Exemplo
Um engenheiro de segurança sobe o ambiente de `docker/docker-compose/` localmente para testar uma regra customizada de detecção de escrita em diretórios de binários e inspecionar o evento renderizado no `falcosidekick-ui`.

## Limites e trade-offs
O ambiente em `docker/docker-compose/` é projetado para demonstração e testes rápidos; para clusters Kubernetes produtivos, utilize os Helm charts oficiais de `falcosecurity/charts` com autenticação e persistência adequadas.

## Como verificar
Conferi a subseção Demo Environment no README oficial de falcosecurity/falco.

## Conexões
- [[falco-production-deployment-checklist-and-setup]] — Veja também: Recomendações oficiais antes do deploy em produção: compatibilidade, metas, performance e SIEM.
- [[falco-cmake-modern-bpf-build-and-unit-tests]] — Veja também: Compilação a partir do código-fonte com CMake, driver Modern BPF (`BUILD_FALCO_MODERN_BPF`) e testes.

## Fontes
- [Falco — GitHub README](https://raw.githubusercontent.com/falcosecurity/falco/master/README.md) — Visão geral do Falco (segurança em tempo de execução no kernel Linux graduada na CNCF, observação de syscalls com metadados de container/Kubernetes, 5 repositórios core, ambiente demo, auditorias em ./audits/ e build CMake com Modern BPF).; consultado em 2026-10-03.
- [Falco — Repositório Oficial no GitHub](https://github.com/falcosecurity/falco) — Repositório oficial do Falco na CNCF com código-fonte C++, chart/falco, docker/docker-compose/ e audits/.; consultado em 2026-10-03.
