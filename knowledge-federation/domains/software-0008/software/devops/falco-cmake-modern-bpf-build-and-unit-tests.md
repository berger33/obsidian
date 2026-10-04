---
id: software.devops.tranche03.000247
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

# Compilação a partir do código-fonte com CMake, driver Modern BPF (`BUILD_FALCO_MODERN_BPF`) e testes

## Em uma frase
As seções `Building` e `Testing` do README apontam para o guia oficial de compilação (`falco.org/docs/developer-guide/source/`) e demonstram o comando exato de `cmake` para habilitar dependências embutidas, drivers, Modern BPF e testes unitários: `cmake -DUSE_BUNDLED_DEPS=ON -DBUILD_DRIVER=ON -DBUILD_FALCO_MODERN_BPF=ON -DCREATE_TEST_TARGETS=ON -DBUILD_FALCO_UNIT_TESTS=ON ..`, seguido de `make -j$(($nproc-1)) falco_unit_tests` e `sudo ./unit_tests/falco_unit_tests`, registrando ainda que os testes de regressão foram movidos para o repositório `falcosecurity/testing`.

## Por que importa
A flag `-DBUILD_FALCO_MODERN_BPF=ON` destaca o suporte ao driver Modern BPF (eBPF moderno embutido no binário), que elimina a necessidade de compilar módulos de kernel fora da árvore ou baixar probes pré-compilados para cada versão exata de kernel em kernels Linux modernos.

## Como funciona
Ao compilar o Falco a partir do código-fonte para desenvolvimento ou validação em kernels recentes, habilite `-DBUILD_FALCO_MODERN_BPF=ON` e `-DBUILD_FALCO_UNIT_TESTS=ON` e execute a suíte `falco_unit_tests`.

## Exemplo
Um desenvolvedor compila o Falco com soporte a Modern BPF e valida todas as asserções em `./unit_tests/falco_unit_tests` antes de submeter uma alteração ao projeto.

## Limites e trade-offs
A execução completa de `./unit_tests/falco_unit_tests` utiliza `sudo` no exemplo oficial porque certos testes interagem com recursos privilegiados do sistema; execute-os em máquinas virtuais ou ambientes de CI isolados.

## Como verificar
Conferi as seções Building e Testing no README oficial de falcosecurity/falco.

## Conexões
- [[falco-demo-environment-falcosidekick-ui-and-redis]] — Veja também: Ambiente de demonstração com Docker Compose: Falco, Falcosidekick, Falcosidekick-UI e Redis.
- [[falco-security-audits-and-vulnerability-reporting]] — Veja também: Auditorias independentes em ./audits/ e relato de vulnerabilidades em falco e libs.

## Fontes
- [Falco — GitHub README](https://raw.githubusercontent.com/falcosecurity/falco/master/README.md) — Visão geral do Falco (segurança em tempo de execução no kernel Linux graduada na CNCF, observação de syscalls com metadados de container/Kubernetes, 5 repositórios core, ambiente demo, auditorias em ./audits/ e build CMake com Modern BPF).; consultado em 2026-10-03.
- [Falco Documentation — Getting Started & Setup](https://falco.org/docs/getting-started/) — Documentação oficial do Falco para início rápido, implantação em produção e compilação a partir do código-fonte.; consultado em 2026-10-03.
