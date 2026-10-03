---
id: software.devops.tranche11.001037
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
fontes: ["https://docs.stakater.com/reloader/latest/", "https://raw.githubusercontent.com/stakater/Reloader/master/README.md", "https://github.com/stakater/Reloader"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Operação do Reloader em produção: escopo de namespaces, ignorar tipos de recursos, eleição de líder HA e métricas Prometheus

## Em uma frase
Em clusters corporativos, o Reloader pode ser restrito a um único namespace ou a um subconjunto selecionado por labels, desabilitar globalmente a observação de `Secrets` (`ignoreSecrets`) ou `ConfigMaps` (`ignoreConfigMaps`), operar em alta disponibilidade com múltiplas réplicas e eleição de líder e expor a métrica Prometheus **`reloader_reload_executed_total`**.

## Por que importa
Em clusters multi-tenant com restrições de RBAC, um operador de equipe pode precisar rodar uma instância do Reloader restrita apenas ao seu namespace ou observar apenas `ConfigMaps` sem permissão de leitura sobre objetos `Secret`. Já em nível de plataforma, rodar múltiplas réplicas com leader election garante que a rotação de segredos não pare se um nó cair.

## Como funciona
Conforme descreve o guia oficial (`docs.stakater.com/reloader/latest/`): (1) por padrão o Reloader observa tanto `Secrets` quanto `ConfigMaps` em todos os namespaces, mas pode-se desativar um dos tipos com `reloader.ignoreSecrets: true` ou `reloader.ignoreConfigMaps: true` no Helm chart; (2) o escopo pode ser limitado a um namespace específico (`watchGlobally: false` / `--Namespaces-to-ignore` / seletores de namespace e recursos); (3) múltiplas réplicas podem ser executadas com **leader election** habilitada para alta disponibilidade; e (4) o controlador expõe métricas Prometheus — em especial o contador `reloader_reload_executed_total` — rastreando cada reload executado.

## Exemplo
```yaml
# Exemplo de values.yaml do Helm chart do Reloader habilitando múltiplas réplicas com leader election e métricas
reloader:
  watchGlobally: true
  ignoreSecrets: false
  ignoreConfigMaps: false
  enableHA: true
  deployment:
    replicas: 2
  serviceMonitor:
    enabled: true
```

## Limites e trade-offs
Se você rodar múltiplas réplicas do Reloader (`replicas: 2` ou mais) **sem** habilitar a eleição de líder (`enableHA: true`), todas as réplicas processarão o mesmo evento de watch simultaneamente e tentarão aplicar patches concorrentes nos mesmos Deployments.

## Como verificar
Consulte o endpoint `/metrics` do pod do Reloader (`curl -s http://localhost:9090/metrics | grep reloader_reload_executed_total`) e verifique o objeto `Lease` de eleição de líder no namespace `reloader`.

## Conexões
- [[reloader-pausa-deployments-pause-period-alertas-webhook]] — Veja também: Estabilidade operacional no Reloader: janela de pausa (pause-period) e alertas de reload (Slack, Teams, Google Chat e Webhook).
- [[reloader-evolucao-v2-operator-sdk-workloads-suportados]] — Veja também: Arquitetura do Reloader v2 (Operator SDK) e matriz de workloads suportados (Deployment, StatefulSet, DaemonSet, CronJob, Job e DeploymentConfig).
- [[reloader-controlador-kubernetes-rollout-configmaps-secrets]] — Referência cruzada direta com reloader-controlador-kubernetes-rollout-configmaps-secrets.

## Fontes
- [Stakater Reloader GitHub — README.md (Reloader v2 Operator SDK, Annotations, Search/Match, Argo Rollouts, Pause & CSI Support)](https://docs.stakater.com/reloader/latest/) — README oficial do stakater/Reloader detalhando anotações auto/named/search+match/ignore, estratégia restart para Argo Rollouts, alertas webhook, pause-period e integração com Secrets Store CSI Driver; consultado em 2026-10-03.
- [Stakater Reloader Official Documentation — Overview & Mechanics (Watch API, SHA1 Data Check, Workloads & GitOps)](https://raw.githubusercontent.com/stakater/Reloader/master/README.md) — Documentação oficial do Reloader explicando a detecção de mudança de dados reais via watch API, patch SHA1 no pod template, workloads suportados e integração com ESO, Sealed Secrets, cert-manager e Argo CD; consultado em 2026-10-03.
- [Stakater Reloader — Official GitHub Repository](https://github.com/stakater/Reloader) — Repositório oficial Apache-2.0 do Stakater Reloader; consultado em 2026-10-03.
