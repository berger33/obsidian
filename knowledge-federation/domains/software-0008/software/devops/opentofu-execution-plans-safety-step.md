---
id: software.devops.tranche01.000033
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-25.md"
fontes: ["https://raw.githubusercontent.com/opentofu/opentofu/main/README.md", "https://github.com/opentofu/opentofu"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Planos de execução (`Execution Plans`): separação entre planejar e aplicar mudanças

## Em uma frase
O segundo item da seção Key features no README oficial apresenta **Execution Plans**: o OpenTofu possui uma etapa explícita de planejamento ("planning" step) na qual gera um plano de execução que mostra exatamente o que a ferramenta fará quando você chamar `apply`, permitindo evitar surpresas no momento em que o OpenTofu manipula a infraestrutura.

## Por que importa
Em operações de infraestrutura, certas alterações de parâmetros exigem destruir e recriar um recurso (como uma instância ou banco de dados) em vez de atualizá-lo no lugar; inspecionar o plano de execução antes do `apply` impede destruições acidentais em produção.

## Como funciona
Gere e revise sempre o plano de execução antes de aplicar mudanças — especialmente em pipelines de CI/CD, onde o plano pode ser anexado ao Pull Request para aprovação humana antes da etapa de `apply`.

## Exemplo
Se uma mudança de configuração implicar substituir ou modificar recursos existentes, o plano de execução expõe essas ações antecipadamente antes de tocar na API do provedor.

## Limites e trade-offs
Um plano de execução reflete o estado da infraestrutura no momento em que foi calculado; se recursos forem alterados fora do OpenTofu entre o planejamento e a aplicação, o estado real terá mudado.

## Como verificar
Conferi o item Execution Plans na seção Key features do README oficial de `opentofu/opentofu`.

## Conexões
- [[opentofu-declarative-infrastructure-as-code]] — Veja também: Infraestrutura como Código (IaC): sintaxe declarativa de alto nível, versionamento e reutilização.
- [[opentofu-resource-dependency-graph-parallelism]] — Veja também: Grafo de recursos (`Resource Graph`) e paralelização automática de operações independentes.

## Fontes
- [OpenTofu — README oficial](https://raw.githubusercontent.com/opentofu/opentofu/main/README.md) — README oficial do OpenTofu com definição OSS, quatro Key features (IaC, Execution Plans, Resource Graph e Change Automation), Nightly Builds (30 dias e latest.json), Security Policy, liaison@opentofu.org, Registry Policy, reuniões e licença MPL-2.0.; consultado em 2026-10-03.
- [Repositório oficial opentofu/opentofu](https://github.com/opentofu/opentofu) — Repositório oficial do OpenTofu no GitHub com código-fonte, RELEASE.md, CONTRIBUTING.md e LICENSE (MPL-2.0).; consultado em 2026-10-03.
