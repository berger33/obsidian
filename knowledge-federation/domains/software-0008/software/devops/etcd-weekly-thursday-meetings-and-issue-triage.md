---
id: software.devops.tranche03.000299
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
fontes: ["https://raw.githubusercontent.com/etcd-io/etcd/main/README.md", "https://github.com/etcd-io/etcd"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Reuniões semanais às quintas-feiras (11:00 AM PT) alternando comunidade e triagem de issues

## Em uma frase
A seção `Contact` e a subseção `Community meetings` do README informam que contribuidores e mantenedores do etcd reúnem-se toda semana às quintas-feiras às `11:00 AM` (USA Pacific), alternando entre reuniões comunitárias (`community meetings`) e reuniões de triagem de issues (`issue triage meetings`), com liderança rotativa entre mantenedores do etcd e líderes do `sig-etcd`, pauta em documento compartilhado, gravações no YouTube e comunicação na lista `etcd-dev` (`groups.google.com/g/etcd-dev`) e no canal `#sig-etcd` no Slack do Kubernetes.

## Por que importa
O próprio README ressalta que as reuniões de triagem de issues são abertas a qualquer contribuidor — não sendo necessário ser revisor ou aprovador para ajudar — e funcionam como excelente porta de entrada para novos participantes.

## Como funciona
Junte-se à lista `etcd-dev` para receber os convites de calendário, participe do canal `#sig-etcd` no Slack do Kubernetes e acompanhe as reuniões de quinta-feira às `11:00 AM PT`.

## Exemplo
Um novo contribuidor participa da reunião de triagem de quinta-feira para entender o contexto de issues abertas antes de submeter seu primeiro pull request.

## Limites e trade-offs
Adicione tópicos sugeridos previamente ao documento compartilhado de notas da reunião (`shared Google doc`) para que entrem na pauta da semana.

## Como verificar
Conferi a seção Contact e a subseção Community meetings no README oficial de etcd-io/etcd.

## Conexões
- [[etcd-maintainers-culture-and-community-membership]] — Veja também: Cultura de manutenção em OWNERS e responsabilidades em community-membership.md.
- [[etcd-ci-verification-codeql-coverage-and-scorecard]] — Veja também: Verificação contínua no repositório: workflows de testes, Codecov, CodeQL e OpenSSF Scorecard.

## Fontes
- [etcd — GitHub README](https://raw.githubusercontent.com/etcd-io/etcd/main/README.md) — Visão geral do etcd (banco chave-valor distribuído via consenso Raft, pilares Simple/Secure/Fast/Reliable, testes de robustez, 7 pacotes Go v3, portas IANA 2379/2380, cluster local via goreman/Procfile com learner node e reuniões).; consultado em 2026-10-03.
- [etcd — Repositório Oficial no GitHub](https://github.com/etcd-io/etcd) — Repositório oficial do etcd na CNCF com código-fonte Go, etcdctl/, tests/robustness/, Procfile, OWNERS e ADOPTERS.md.; consultado em 2026-10-03.
