---
id: software.devops.tranche11.001050
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-11.md"
fontes: ["https://raw.githubusercontent.com/FairwindsOps/goldilocks/master/README.md", "https://goldilocks.docs.fairwinds.com/advanced/", "https://goldilocks.docs.fairwinds.com/installation/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Integração do Goldilocks com Polaris e Pluto em fluxos contínuos de governança e FinOps no Kubernetes

## Em uma frase
Dentro do ecossistema open-source da Fairwinds, o **Goldilocks** (dimensionamento de CPU/memória baseado em uso real via VPA) complementa diretamente o **Polaris** (que audita e cobra a presença de `cpuRequestsMissing`, `memoryRequestsMissing`, `cpuLimitsMissing` e `memoryLimitsMissing`) e o **Pluto** (detecção de `apiVersions` depreciadas).

## Por que importa
Exigir via política de admissão (Polaris, Kyverno ou Gatekeeper) que todo container declare `resources.requests` e `resources.limits` impede que pods subam sem limites, mas faz com que desenvolvedores copiem e colem valores arbitrários (`cpu: 1000m, memory: 2Gi`) apenas para passar no gate de CI. O Goldilocks fecha o ciclo fornecendo os números reais baseados na telemetria do VPA para calibrar esses manifestos.

## Como funciona
Conforme descreve o README oficial (`FairwindsOps/goldilocks`), as ferramentas atuam em etapas complementares do ciclo de vida: (1) no CI/CD e na admissão do cluster, o **Polaris** valida se os manifestos declaram requests/limits e boas práticas de segurança, e o **Pluto** garante que nenhuma API depreciada (incluindo versões antigas de `autoscaling`) seja implantada; (2) no cluster em execução, o **Goldilocks** cria os VPAs em modo `Off` e coleta o perfil real de consumo; e (3) periodicamente, a equipe extrai o relatório JSON via `goldilocks summary` (ou visualiza o dashboard) e atualiza os valores de `requests` e `limits` no repositório GitOps.

## Exemplo
```bash
# Extrair via jq os containers cujos requests atuais diferem das recomendações target do VPA no Goldilocks summary
goldilocks summary | jq '.Namespaces | to_entries[] | {namespace: .key, workloads: .value.workloads}'
```

## Limites e trade-offs
As recomendações do VPA recém-criadas nos primeiros minutos após o deploy refletem apenas o consumo imediato de inicialização; aguarde pelo menos 24 horas (ou um ciclo completo de pico de tráfego de negócio, preferencialmente com histórico do Prometheus integrado ao VPA Recommender) antes de reduzir `limits` de memória em produção com base no Goldilocks.

## Como verificar
Compare a saída JSON de `goldilocks summary` com o relatório de auditoria do Polaris (`polaris audit --format=pretty`) para confirmar que todos os containers possuem requests/limits definidos e alinhados ao consumo observado.

## Conexões
- [[goldilocks-exclusao-containers-por-workload-anotacoes-granulares]] — Veja também: Exclusão granular de containers e desativação por workload individual no Goldilocks.
- [[goldilocks-dimensionamento-requests-limits-vpa-kubernetes]] — Referência cruzada direta com goldilocks-dimensionamento-requests-limits-vpa-kubernetes.
- [[polaris-motor-politicas-validacao-remediacao-kubernetes]] — Referência cruzada direta com polaris-motor-politicas-validacao-remediacao-kubernetes.
- [[pluto-deteccao-apiversions-depreciadas-removidas-kubernetes]] — Referência cruzada direta com pluto-deteccao-apiversions-depreciadas-removidas-kubernetes.

## Fontes
- [Fairwinds Goldilocks Official Documentation — Installation & Requirements (VPA Recommender, metrics-server, Helm & GKE)](https://raw.githubusercontent.com/FairwindsOps/goldilocks/master/README.md) — Documentação oficial de instalação do Goldilocks detalhando requisitos (VPA Recommender sem webhook, metrics-server, Prometheus opcional, GKE Standard vs Autopilot), Helm chart, manifestos e habilitação de namespaces; consultado em 2026-10-03.
- [Fairwinds Goldilocks Official Documentation — Advanced Usage & README (Controller Flags, Metrics, vpa-update-mode, vpa-resource-policy & v4.15.0+ Images)](https://goldilocks.docs.fairwinds.com/advanced/) — Guia oficial de uso avançado e README do Goldilocks cobrindo flags do controlador, métricas Prometheus, anotações vpa-update-mode e vpa-resource-policy, comandos summary/dashboard, --exclude-containers e imagens assinadas v4.15.0+; consultado em 2026-10-03.
- [Fairwinds Goldilocks — Official Documentation & Repository](https://goldilocks.docs.fairwinds.com/installation/) — Documentação e repositório oficial do Fairwinds Goldilocks; consultado em 2026-10-03.
