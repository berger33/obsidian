---
id: software.devops.tranche03.000244
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

# Extensão além de syscalls com falcosecurity/plugins e gerenciamento via falcoctl

## Em uma frase
Na descrição dos repositórios core em `The Falco Project`, o README destaca que o repositório `falcosecurity/plugins` suporta a integração com serviços externos por meio de plugins que estendem as capacidades do Falco **além de syscalls e eventos de contêineres**, enquanto o `falcosecurity/falcoctl` fornece a ferramenta de linha de comando projetada para gerenciar e interagir com o Falco (como instalação e atualização de regras e plugins).

## Por que importa
Em ambientes cloud-native, ameaças não ocorrem apenas dentro das syscalls do kernel Linux: ações maliciosas também aparecem nos logs de auditoria da API do Kubernetes, em trilhas de auditoria da nuvem (como AWS CloudTrail) ou em eventos de provedores de identidade e código; os plugins do Falco aplicam o mesmo motor de regras sobre essas fontes externas.

## Como funciona
Combine a monitoração de syscalls nos nós Linux com instâncias do Falco equipadas com plugins de `falcosecurity/plugins` (instalados e atualizados via `falcoctl`) para correlacionar eventos de auditoria de nuvem e Kubernetes.

## Exemplo
Uma instância do Falco usa um plugin oficial para avaliar eventos de auditoria de nuvem em tempo real com a mesma sintaxe de regras usada para monitorar syscalls nos nós.

## Limites e trade-offs
Evite misturar na mesma instância crítica de syscall do nó plugins externos de alto volume de rede; separe as instâncias de coleta de logs/APIs externas dos DaemonSets de kernel quando necessário.

## Como verificar
Conferi os itens falcosecurity/plugins e falcosecurity/falcoctl na lista de core repositories em The Falco Project no README oficial de falcosecurity/falco.

## Conexões
- [[falco-five-core-repositories-modular-ecosystem]] — Veja também: Arquitetura modular da organização falcosecurity: libs, rules, plugins, falcoctl e charts.
- [[falco-production-deployment-checklist-and-setup]] — Veja também: Recomendações oficiais antes do deploy em produção: compatibilidade, metas, performance e SIEM.

## Fontes
- [Falco — GitHub README](https://raw.githubusercontent.com/falcosecurity/falco/master/README.md) — Visão geral do Falco (segurança em tempo de execução no kernel Linux graduada na CNCF, observação de syscalls com metadados de container/Kubernetes, 5 repositórios core, ambiente demo, auditorias em ./audits/ e build CMake com Modern BPF).; consultado em 2026-10-03.
- [Falco Documentation — Getting Started & Setup](https://falco.org/docs/getting-started/) — Documentação oficial do Falco para início rápido, implantação em produção e compilação a partir do código-fonte.; consultado em 2026-10-03.
