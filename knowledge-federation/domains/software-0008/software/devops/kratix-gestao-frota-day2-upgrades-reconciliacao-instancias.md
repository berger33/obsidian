---
id: software.devops.tranche12.001108
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-12.md"
fontes: ["https://docs.kratix.io/main/quick-start", "https://raw.githubusercontent.com/syntasso/kratix/main/README.md", "https://github.com/syntasso/kratix"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Kratix: Gestão de Frota no Dia 2 e Atualização em Massa de Instâncias via Promise

## Em uma frase
No Kratix, atualizar a definição de uma Promise (como corrigir uma CVE de imagem base, elevar o número padrão de réplicas ou adicionar políticas de rede) dispara automaticamente a reexecução dos workflows para todas as Resource Requests existentes daquela Promise.

## Por que importa
Em plataformas tradicionais baseadas em scaffolding ou templates de repositório, corrigir uma vulnerabilidade em 300 bancos de dados exige abrir 300 Pull Requests e depender da ação manual de dezenas de squads consumidoras.

## Como funciona
Quando o manifesto da `Promise` é atualizado no cluster de plataforma (`kubectl apply -f promise-ha.yaml`), o controlador do Kratix detecta a mudança de geração da Promise e reconcilia cada Resource Request ativa ligada àquela Promise, reexecutando os pipelines `resource.configure` e atualizando os `WorkPlacements` no State Store para toda a frota de uma só vez.

## Exemplo
```bash
kubectl apply -f https://raw.githubusercontent.com/syntasso/promise-postgresql/refs/heads/main/promise-ha.yaml
kubectl get pods -l kratix.io/promise-name=postgresql --watch
kubectl get pods -l application=spilo -A
```

## Limites e trade-offs
Introduzir uma alteração incompatível ou destrutiva no pipeline de uma Promise e aplicá-la diretamente em produção propaga a regressão simultaneamente para todas as instâncias existentes da frota.

## Como verificar
Teste atualizações de Promise primeiro em ambiente de homologação, acompanhe a reexecução dos Jobs de pipeline de cada instância e monitore o rollout gradual nos clusters de destino.

## Conexões
- [[kratix-dependencies-promise-workflows-fleet-bootstrapping]] — Veja também: Kratix: Dependências de Promise e Workflows de Bootstrapping de Frota.
- [[kratix-compound-promises-composicao-paved-roads-multicamada]] — Veja também: Kratix: Compound Promises e Composição de Paved Roads Multicamada.

## Fontes
- [Kratix GitHub — README.md & Official Quick Start Guide (Promises, Destinations, State Stores & Fleet Management)](https://docs.kratix.io/main/quick-start) — README oficial do syntasso/kratix (Apache-2.0) e guia Quick Start detalhando Promises, Resource Requests, Workflows em containers, State Stores (SeaweedFS/Git), Flux e atualização de frota no Dia 2; consultado em 2026-10-03.
- [Kratix Official Documentation — Quick Start & Platform Concepts](https://raw.githubusercontent.com/syntasso/kratix/main/README.md) — Documentação oficial do Kratix sobre publicação de Promises, status.connectionDetails, Compound Promises e agendamento multi-cluster; consultado em 2026-10-03.
- [Syntasso Kratix — Official GitHub Repository](https://github.com/syntasso/kratix) — Repositório oficial Apache-2.0 do Kratix; consultado em 2026-10-03.
