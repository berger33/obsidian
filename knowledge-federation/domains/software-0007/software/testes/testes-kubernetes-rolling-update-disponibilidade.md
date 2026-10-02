---
id: software.testes.tranche07.000137
tipo: tecnica
dominio: software
subdominio: testes
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-01
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-07.md"
fontes: ["https://kubernetes.io/docs/concepts/workloads/controllers/deployment/", "https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Teste de disponibilidade durante rolling update Kubernetes", "Teste: Teste de disponibilidade durante rolling update Kubernetes"]
lote: software-testes-2000-0001
---

# Teste de disponibilidade durante rolling update Kubernetes

## Em uma frase
Exercite uma atualização progressiva e confirme estado do Deployment, prontidão dos Pods e continuidade das operações esperadas.

## Por que importa
Rollout configurado incorretamente pode reduzir réplicas disponíveis ou enviar tráfego a instâncias não prontas, interrompendo usuários.

## Como funciona
Em cluster descartável ou ambiente autorizado, registre imagem e réplicas iniciais, aplique mudança, observe condições e rollout status, e faça chamadas funcionais durante substituição. Valide estratégia maxUnavailable/maxSurge conforme desenho do workload.

## Exemplo
Atualize uma versão de serviço com três réplicas enquanto um probe sintético chama endpoint de leitura; confirme que novas réplicas ficam prontas antes de retirar antigas e que a versão esperada termina disponível.

## Limites e trade-offs
Disponibilidade depende de réplicas, recursos, probes e compatibilidade entre versões. Zero downtime não é garantido por rolling update isoladamente; migrações incompatíveis precisam de plano separado.

## Como verificar
Capture eventos, Ready/Available, erros e latência durante o rollout; interrompa ou reverta quando critério de parada for atingido e confirme que nenhuma requisição de teste alterou estado de negócio inesperado.

## Conexões
- [[deployment-rolling-update-kubernetes]] — aprofundamento relacionado.
- [[testes-probes-startup-liveness-readiness]] — aprofundamento relacionado.

## Fontes
- [Kubernetes — Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) — rollouts progressivos, status, revisão e rollback de Deployment; consultado em 2026-10-01.
- [Kubernetes — Performing a Rolling Update](https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/) — verificação de update e exercício de rollback; consultado em 2026-10-01.
