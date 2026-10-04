---
id: software.devops.tranche11.001060
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
fontes: ["https://raw.githubusercontent.com/FairwindsOps/polaris/master/README.md", "https://polaris.docs.fairwinds.com/admission-controller/", "https://polaris.docs.fairwinds.com/infrastructure-as-code/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Polaris Dashboard: visibilidade contínua de conformidade no cluster e combinação dos três modos de execução

## Em uma frase
O **Polaris Dashboard** roda em modo somente-leitura (ou ao lado do webhook) para auditar continuamente os recursos implantados no cluster Kubernetes contra as políticas de código, exibindo um *scorecard* visual com notas e detalhamento de falhas `danger` e `warning` por namespace e controlador.

## Por que importa
Antes de ligar o Validating Webhook do Polaris em modo de bloqueio em um cluster produtivo existente, as equipes de plataforma precisam enxergar qual seria o raio de impacto sobre os workloads atuais e acompanhar a evolução da nota de conformidade de cada equipe ao longo do tempo.

## Como funciona
Conforme descrevem o README oficial e a arquitetura do Polaris (`FairwindsOps/polaris`), o Dashboard consulta a API do Kubernetes (ou pode ser aberto localmente apontando para o `kubeconfig` atual via `polaris dashboard`), executa as mais de 30 políticas embutidas e eventuais `customChecks` sobre todos os workloads ativos e agrupa os resultados por categoria (Security, Efficiency, Reliability) e por namespace. Isso permite uma jornada de adoção em três passos sem atrito: (1) visibilidade não intrusiva com o **Dashboard**; (2) feedback preventivo no Pull Request com a **CLI (`polaris audit` / `polaris fix`)**; e (3) bloqueio definitivo de regressões no cluster com o **Admission Controller**.

## Exemplo
```bash
# Iniciar o Polaris Dashboard localmente na porta 8080 auditando o cluster atual do kubeconfig
polaris dashboard --port 8080

# Ou instalar apenas o Polaris Dashboard dentro do cluster via Helm
helm upgrade --install polaris fairwinds-stable/polaris \
  --namespace polaris \
  --create-namespace \
  --set dashboard.enable=true \
  --set webhook.enable=false
```

## Limites e trade-offs
O Polaris foca na validação da configuração declarativa dos controladores de workload (Deployments, DaemonSets, StatefulSets, Jobs, CronJobs); para detectar recursos órfãos/inutilizados (como Services sem Endpoints, Secrets/ConfigMaps/ServiceAccounts não referenciados ou portas divergentes entre Service e Pod), complemente o Polaris com um sanitizador de cluster vivo como o **Popeye**.

## Como verificar
Acesse `http://localhost:8080` após iniciar `polaris dashboard` (ou via `kubectl -n polaris port-forward svc/polaris-dashboard 8080:80`) e inspecione a pontuação percentual do cluster.

## Conexões
- [[polaris-migracao-registro-imagens-assinadas-imutaveis-v10-2]] — Veja também: Migração de registro e imagens imutáveis assinadas no Fairwinds Polaris (v10.2.0+).
- [[polaris-motor-politicas-validacao-remediacao-kubernetes]] — Referência cruzada direta com polaris-motor-politicas-validacao-remediacao-kubernetes.
- [[polaris-admission-controller-validating-mutating-webhook]] — Referência cruzada direta com polaris-admission-controller-validating-mutating-webhook.
- [[popeye-linter-cluster-kubernetes-vivo-readonly]] — Referência cruzada direta com popeye-linter-cluster-kubernetes-vivo-readonly.

## Fontes
- [Fairwinds Polaris Official Documentation — Infrastructure as Code (polaris audit, polaris fix, Exit Code Flags, Helm & GitHub Action)](https://raw.githubusercontent.com/FairwindsOps/polaris/master/README.md) — Guia oficial de Infrastructure as Code do Polaris cobrindo polaris audit, polaris fix, --set-exit-code-on-danger, --set-exit-code-below-score, auditoria de Helm charts e setup-polaris GitHub Action; consultado em 2026-10-03.
- [Fairwinds Polaris Official Documentation — Admission Controller & README (Validating/Mutating Webhook, 19 Default Mutations & v10.2.0+ Images)](https://polaris.docs.fairwinds.com/admission-controller/) — Documentação oficial do Admission Controller e README do Polaris detalhando Validating Webhook (danger vs warning), Mutating Webhook (--set webhook.mutate=true com 19 mutações padrão), políticas JSON Schema e imagens imutáveis v10.2.0+; consultado em 2026-10-03.
- [Fairwinds Polaris — Official Documentation & Repository](https://polaris.docs.fairwinds.com/infrastructure-as-code/) — Documentação e repositório oficial do Fairwinds Polaris; consultado em 2026-10-03.
