---
id: software.devops.tranche11.001042
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
fontes: ["https://goldilocks.docs.fairwinds.com/installation/", "https://raw.githubusercontent.com/FairwindsOps/goldilocks/master/README.md", "https://goldilocks.docs.fairwinds.com/advanced/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Requisitos de infraestrutura do Goldilocks: VPA Recommender isolado (sem webhook), metrics-server, Prometheus e GKE

## Em uma frase
Para operar com segurança, o Goldilocks requer apenas o componente **Recommender** do Vertical Pod Autoscaler (dispensando o *VPA Updater* e o *Admission Webhook*), o **`metrics-server`** (com suporte opcional ao Prometheus para maior precisão histórica) e, em clusters GKE Standard, a ativação explícita de `--enable-vertical-pod-autoscaling`.

## Por que importa
Uma instalação completa padrão do Vertical Pod Autoscaler inclui três binários: `recommender`, `updater` e `admission-controller`. Instalar o webhook de admissão do VPA sem planejamento adequado pode causar mutações ou reinicializações inesperadas em clusters produtivos. Saber que o Goldilocks precisa **apenas do `recommender`** permite adotar a ferramenta com risco zero de impacto nos workloads.

## Como funciona
Conforme destaca a seção *Important Note about VPA* do guia oficial de instalação (`goldilocks.docs.fairwinds.com/installation/`): (1) se você instalar o VPA através do chart do Goldilocks (habilitando o sub-chart `vpa.enabled=true`) ou do Fairwinds VPA Helm Chart, **apenas o VPA Recommender será instalado**, omitindo o updater e o admission webhook; (2) o VPA Recommender exige o `metrics-server`, mas suporta opcionalmente o **Prometheus** como backend de dados para recomendações baseadas em janelas históricas mais longas; e (3) no **Google Kubernetes Engine (GKE)**, o VPA já vem habilitado por padrão em clusters Autopilot, mas em clusters GKE Standard deve ser habilitado via `gcloud container clusters update [CLUSTER-NAME] --enable-vertical-pod-autoscaling` (observando que o VPA gerenciado do GKE não suporta usar o Prometheus como backend de dados).

## Exemplo
```bash
# Habilitar o Vertical Pod Autoscaler nativo em um cluster GKE Standard antes de instalar o Goldilocks
gcloud container clusters update meu-cluster-prod \
  --enable-vertical-pod-autoscaling \
  --region us-central1
```

## Limites e trade-offs
Ao utilizar o VPA gerenciado pelo plano de controle do GKE (`--enable-vertical-pod-autoscaling`), você economiza recursos de executar o pod do VPA Recommender dentro do seu cluster, porém perde a opção de conectar o VPA Recommender a uma instância customizada do Prometheus.

## Como verificar
Verifique a presença das CRDs do VPA no cluster com `kubectl get crd verticalpodautoscalers.autoscaling.k8s.io` e confirme que `kubectl top pods -A` (via `metrics-server`) retorna métricas válidas.

## Conexões
- [[goldilocks-dimensionamento-requests-limits-vpa-kubernetes]] — Veja também: Fairwinds Goldilocks: utilitário Kubernetes para dimensionamento (right-sizing) de resource requests e limits via VPA.
- [[goldilocks-controlador-flags-labels-namespaces-metricas]] — Veja também: Controlador do Goldilocks: precedência de labels sobre flags de CLI, --on-by-default, --ignore-controller-kind e métricas Prometheus.
- [[goldilocks-modos-atualizacao-vpa-update-mode-resource-policy]] — Referência cruzada direta com goldilocks-modos-atualizacao-vpa-update-mode-resource-policy.

## Fontes
- [Fairwinds Goldilocks Official Documentation — Installation & Requirements (VPA Recommender, metrics-server, Helm & GKE)](https://goldilocks.docs.fairwinds.com/installation/) — Documentação oficial de instalação do Goldilocks detalhando requisitos (VPA Recommender sem webhook, metrics-server, Prometheus opcional, GKE Standard vs Autopilot), Helm chart, manifestos e habilitação de namespaces; consultado em 2026-10-03.
- [Fairwinds Goldilocks Official Documentation — Advanced Usage & README (Controller Flags, Metrics, vpa-update-mode, vpa-resource-policy & v4.15.0+ Images)](https://raw.githubusercontent.com/FairwindsOps/goldilocks/master/README.md) — Guia oficial de uso avançado e README do Goldilocks cobrindo flags do controlador, métricas Prometheus, anotações vpa-update-mode e vpa-resource-policy, comandos summary/dashboard, --exclude-containers e imagens assinadas v4.15.0+; consultado em 2026-10-03.
- [Fairwinds Goldilocks — Official Documentation & Repository](https://goldilocks.docs.fairwinds.com/advanced/) — Documentação e repositório oficial do Fairwinds Goldilocks; consultado em 2026-10-03.
