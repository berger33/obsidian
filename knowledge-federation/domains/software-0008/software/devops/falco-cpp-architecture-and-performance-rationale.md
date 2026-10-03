---
id: software.devops.tranche03.000249
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

# Motivação arquitetural do uso de C++ no motor do Falco e nas bibliotecas de captura

## Em uma frase
A seção `FAQs` (`Why is Falco in C++ rather than Go or {language}?`) e a descrição de `falcosecurity/libs` no README explicam por que o núcleo do Falco e suas bibliotecas de inspeção de syscalls foram escritos em C++: o projeto compartilha a fundação histórica de captura e filtragem de eventos de alta frequência com o ecossistema Sysdig (`libs`), onde o processamento determinístico sem coletor de lixo (GC) e a proximidade com os drivers de kernel/eBPF em C/C++ são essenciais para avaliar milhões de syscalls por segundo com baixo overhead.

## Por que importa
Compreender que o motor central (`falco` e `libs`) é escrito em C++ enquanto ferramentas auxiliares do ecossistema (como `falcoctl`, plugins e integrações cloud-native) utilizam linguagens como Go esclarece a divisão de responsabilidades entre o caminho crítico do kernel e as ferramentas de gerência.

## Como funciona
Ao desenvolver código para o binário principal ou para `falcosecurity/libs`, utilize a toolchain C++/CMake documentada pelo projeto; já para utilitários de controle e automação externa, integre-se via `falcoctl`, plugins ou `falcosidekick`.

## Exemplo
Em um nó sob carga intensa de I/O e rede, o motor C++ do Falco avalia os filtros de eventos diretamente sobre o buffer de captura sem pausas de garbage collection.

## Limites e trade-offs
Ao escrever ou compilar extensões nativas em C/C++, mantenha os testes unitários e verificadores de memória ativos no pipeline de CI.

## Como verificar
Conferi as seções The Falco Project e FAQs no README oficial de falcosecurity/falco.

## Conexões
- [[falco-security-audits-and-vulnerability-reporting]] — Veja também: Auditorias independentes em ./audits/ e relato de vulnerabilidades em falco e libs.
- [[falco-community-channels-and-evolution-governance]] — Veja também: Comunidade no Slack #falco, lista cncf-falco-dev e governança em falcosecurity/evolution.

## Fontes
- [Falco — GitHub README](https://raw.githubusercontent.com/falcosecurity/falco/master/README.md) — Visão geral do Falco (segurança em tempo de execução no kernel Linux graduada na CNCF, observação de syscalls com metadados de container/Kubernetes, 5 repositórios core, ambiente demo, auditorias em ./audits/ e build CMake com Modern BPF).; consultado em 2026-10-03.
- [Falco — Repositório Oficial no GitHub](https://github.com/falcosecurity/falco) — Repositório oficial do Falco na CNCF com código-fonte C++, chart/falco, docker/docker-compose/ e audits/.; consultado em 2026-10-03.
