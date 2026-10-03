---
id: software.devops.tranche02.000105
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-02.md"
fontes: ["https://raw.githubusercontent.com/crossplane/crossplane/main/README.md", "https://github.com/crossplane/crossplane"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Fim de suporte da série v1.20 e transição para o Crossplane v2

## Em uma frase
A subseção `v1.20 end-of-life (EOL)` do README destaca expressamente que, quando a versão `v2.5` for lançada em novembro de 2026, a série `v1.20` atingirá seu EOL e deixará de receber qualquer suporte ou manutenção pelo projeto Crossplane, remetendo às notas de versão da `v2.4.0` e ao grupo `#sig-v2-migration` para detalhes.

## Por que importa
Organizações que ainda mantêm planos de controle na linha 1.x precisam planejar a migração de APIs e composições para a linha 2.x antes do encerramento definitivo do suporte da `v1.20`.

## Como funciona
Audite os clusters que ainda executam `v1.20`, revise as notas de release da série `v2.x` e participe do canal `#sig-v2-migration` caso encontre dúvidas sobre compatibilidade de composições.

## Exemplo
Uma equipe que postergou a saída da `v1.20` cria um plano de migração testado em homologação antes do lançamento da `v2.5` em novembro de 2026.

## Limites e trade-offs
Atualizar entre versões principais (`v1` para `v2`) sem testar previamente os provedores e funções de composição instalados pode interromper a reconciliação de recursos existentes.

## Como verificar
Conferi a subseção v1.20 end-of-life (EOL) e a lista de SIGs no README oficial de `crossplane/crossplane`.

## Conexões
- [[crossplane-maintained-releases-and-eol-schedule]] — Veja também: Tabela de versões mantidas e cronograma de End-of-Life (EOL).
- [[crossplane-public-roadmap-and-triage-process]] — Veja também: Roadmap público, triagem comunitária e natureza estimativa dos milestones.

## Fontes
- [Crossplane — GitHub README](https://raw.githubusercontent.com/crossplane/crossplane/main/README.md) — Visão geral do Crossplane como framework de control planes cloud-native na CNCF, tabela de releases e EOL (v1.20 e v2.2–v2.7), roadmap, reuniões e 14 SIGs.; consultado em 2026-10-03.
- [Crossplane — Repositório Oficial no GitHub](https://github.com/crossplane/crossplane) — Repositório oficial do Crossplane com código-fonte, ADOPTERS.md, contributing/README.md e notas de release.; consultado em 2026-10-03.
