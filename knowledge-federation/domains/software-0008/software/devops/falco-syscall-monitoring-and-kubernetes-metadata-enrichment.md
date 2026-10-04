---
id: software.devops.tranche03.000242
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
fontes: ["https://raw.githubusercontent.com/falcosecurity/falco/master/README.md", "https://falco.org/docs/getting-started/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Observação de syscalls no kernel enriquecida com metadados de container runtime e Kubernetes

## Em uma frase
O segundo parágrafo do README oficial explica que, em seu núcleo, o Falco é um agente de monitoramento e detecção no kernel que observa eventos — como chamadas de sistema (`syscalls`) — com base em regras customizadas, enriquecendo esses eventos com metadados do runtime de contêineres (como `containerd` ou `CRI-O`) e do Kubernetes, de modo que os eventos coletados possam ser analisados fora do host (`off-host`) em sistemas de SIEM ou data lake.

## Por que importa
Um alerta bruto dizendo apenas que o processo `PID 4182` abriu `/etc/shadow` em um nó com centenas de contêineres é insuficiente para resposta rápida; quando o Falco enriquece a syscall com o nome do pod, namespace, imagem do contêiner e labels do Kubernetes e exporta o alerta para um SIEM fora do host, a equipe identifica o serviço comprometido imediatamente e preserva a evidência mesmo que o invasor destrua o nó.

## Como funciona
Configure o Falco integrado ao socket do container runtime e aos metadados do Kubernetes e encaminhe todos os alertas imediatamente para um SIEM ou data lake externo ao host monitorado.

## Exemplo
Um processo dentro de um contêiner tenta executar um binário de mineração ou modificar certificados do sistema; o Falco captura a syscall no kernel, anexa os metadados do pod Kubernetes e envia o alerta para o SIEM central.

## Limites e trade-offs
Nunca armazene os alertas de segurança apenas no disco local do próprio nó monitorado; o envio `off-host` é essencial para preservar a trilha forense.

## Como verificar
Conferi o segundo parágrafo da abertura e a seção Getting Started with Falco no README oficial de falcosecurity/falco.

## Conexões
- [[falco-cloud-native-linux-runtime-security-overview]] — Veja também: Detecção de comportamento anormal em tempo real no kernel Linux graduada na CNCF.
- [[falco-five-core-repositories-modular-ecosystem]] — Veja também: Arquitetura modular da organização falcosecurity: libs, rules, plugins, falcoctl e charts.

## Fontes
- [Falco — GitHub README](https://raw.githubusercontent.com/falcosecurity/falco/master/README.md) — Visão geral do Falco (segurança em tempo de execução no kernel Linux graduada na CNCF, observação de syscalls com metadados de container/Kubernetes, 5 repositórios core, ambiente demo, auditorias em ./audits/ e build CMake com Modern BPF).; consultado em 2026-10-03.
- [Falco Documentation — Getting Started & Setup](https://falco.org/docs/getting-started/) — Documentação oficial do Falco para início rápido, implantação em produção e compilação a partir do código-fonte.; consultado em 2026-10-03.
