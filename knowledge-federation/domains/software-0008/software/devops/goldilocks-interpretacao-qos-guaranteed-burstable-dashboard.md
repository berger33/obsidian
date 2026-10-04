---
id: software.devops.tranche11.001047
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
fontes: ["https://raw.githubusercontent.com/FairwindsOps/goldilocks/master/README.md", "https://goldilocks.docs.fairwinds.com/installation/", "https://goldilocks.docs.fairwinds.com/advanced/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Interpretação das recomendações do Goldilocks Dashboard: classes de QoS Guaranteed versus Burstable no Kubernetes

## Em uma frase
O dashboard do Goldilocks apresenta as métricas do VPA Recommender traduzidas em recomendações práticas de `requests` e `limits` de CPU e memória para duas classes de Qualidade de Serviço (QoS) do Kubernetes: **Guaranteed** (`requests == limits`) e **Burstable** (`requests < limits`).

## Por que importa
O objeto bruto `VerticalPodAutoscaler` no Kubernetes expõe quatro números estatísticos no seu `status.recommendation.containerRecommendations` (`target`, `lowerBound`, `upperBound` e `uncappedTarget`), que muitos desenvolvedores têm dificuldade de converter em blocos YAML `resources:` adequados ao perfil de risco de cada aplicação.

## Como funciona
Quando o usuário acessa o Goldilocks Dashboard (`kubectl -n goldilocks port-forward svc/goldilocks-dashboard 8080:80`) ou gera o relatório, o Goldilocks lê os valores atuais de `resources.requests` e `resources.limits` de cada container do workload e os compara com os cálculos do VPA Recommender: (1) na opção **Guaranteed QoS**, sugere definir `requests` e `limits` iguais ao valor alvo (`target`) do VPA, garantindo que o pod tenha prioridade máxima no kubelet e menor probabilidade de evicção sob pressão de memória no nó; e (2) na opção **Burstable QoS**, sugere `requests` baseados no consumo típico (`lowerBound`/`target`) e `limits` baseados no pico (`upperBound`), permitindo maior densidade de agendamento no cluster com margem para picos transitórios.

## Exemplo
```yaml
# Exemplo de bloco resources ajustado para classe QoS Guaranteed (requests == limits) a partir da recomendação do Goldilocks
resources:
  requests:
    cpu: 250m
    memory: 512Mi
  limits:
    cpu: 250m
    memory: 512Mi
```

## Limites e trade-offs
Para workloads com picos agudos de CPU no boot (como aplicações Java/Spring ou JVM em geral), copiar cegamente um `limit` de CPU estreito pode tornar a inicialização da aplicação muito lenta por *CPU throttling*; nesses casos, avalie manter `requests` de CPU dimensionados pelo Goldilocks e usar `limits` de CPU mais folgados (classe *Burstable*) ou focar a garantia rígida (`requests == limits`) na memória.

## Como verificar
Inspecione o objeto VPA bruto com `kubectl -n minha-app get vpa <nome> -o jsonpath='{.status.recommendation.containerRecommendations}' | jq .` e compare os campos `lowerBound`, `target` e `upperBound` com os fragmentos YAML exibidos no Goldilocks Dashboard.

## Conexões
- [[goldilocks-migracao-registro-imagens-imutaveis-assinadas-v4-15]] — Veja também: Migração de registro e segurança de imagens no Goldilocks (v4.15.0+): Artifact Registry, tags imutáveis e assinatura.
- [[goldilocks-instalacao-manifestos-separados-controller-dashboard]] — Veja também: Instalação do Goldilocks via manifestos Kubernetes separados (controller e dashboard) e RBAC.
- [[goldilocks-dimensionamento-requests-limits-vpa-kubernetes]] — Referência cruzada direta com goldilocks-dimensionamento-requests-limits-vpa-kubernetes.
- [[goldilocks-cli-dashboard-summary-exclusao-containers-sidecars]] — Referência cruzada direta com goldilocks-cli-dashboard-summary-exclusao-containers-sidecars.
- [[polaris-motor-politicas-validacao-remediacao-kubernetes]] — Referência cruzada direta com polaris-motor-politicas-validacao-remediacao-kubernetes.

## Fontes
- [Fairwinds Goldilocks Official Documentation — Installation & Requirements (VPA Recommender, metrics-server, Helm & GKE)](https://raw.githubusercontent.com/FairwindsOps/goldilocks/master/README.md) — Documentação oficial de instalação do Goldilocks detalhando requisitos (VPA Recommender sem webhook, metrics-server, Prometheus opcional, GKE Standard vs Autopilot), Helm chart, manifestos e habilitação de namespaces; consultado em 2026-10-03.
- [Fairwinds Goldilocks Official Documentation — Advanced Usage & README (Controller Flags, Metrics, vpa-update-mode, vpa-resource-policy & v4.15.0+ Images)](https://goldilocks.docs.fairwinds.com/installation/) — Guia oficial de uso avançado e README do Goldilocks cobrindo flags do controlador, métricas Prometheus, anotações vpa-update-mode e vpa-resource-policy, comandos summary/dashboard, --exclude-containers e imagens assinadas v4.15.0+; consultado em 2026-10-03.
- [Fairwinds Goldilocks — Official Documentation & Repository](https://goldilocks.docs.fairwinds.com/advanced/) — Documentação e repositório oficial do Fairwinds Goldilocks; consultado em 2026-10-03.
