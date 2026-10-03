---
id: software.devops.tranche11.001045
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
fontes: ["https://goldilocks.docs.fairwinds.com/advanced/", "https://goldilocks.docs.fairwinds.com/installation/", "https://raw.githubusercontent.com/FairwindsOps/goldilocks/master/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Comandos da CLI do Goldilocks (dashboard, summary, create-vpas, delete-vpas) e exclusão de containers sidecar (--exclude-containers)

## Em uma frase
A CLI do Goldilocks fornece os subcomandos `controller`, `dashboard` (servidor web na porta `8080`), `summary` (exportação das recomendações em JSON), `create-vpas`, `delete-vpas`, `version` e `completion`, permitindo ocultar recomendações de sidecars (como Istio e Linkerd) via **`--exclude-containers`**.

## Por que importa
Em malhas de serviço como Istio ou Linkerd, todo pod possui um container `istio-proxy` ou `linkerd-proxy` injetado automaticamente. Ocultar esses sidecars do relatório do Goldilocks (`--exclude-containers=istio-proxy,linkerd-proxy`) mantém o dashboard e o JSON do `goldilocks summary` focados nos containers da aplicação que a equipe de desenvolvimento controla diretamente.

## Como funciona
Conforme explica a página *Advanced Usage* (`goldilocks.docs.fairwinds.com/advanced/`): (1) embora os subcomandos imperativos `goldilocks create-vpas -n <ns>` e `goldilocks delete-vpas -n <ns>` existam na CLI, a documentação **não recomenda** usar a CLI para gerenciar VPAs em produção porque ela opera em apenas um namespace por execução e não limpa VPAs órfãos automaticamente (papel que cabe ao `goldilocks controller`); (2) em contrapartida, o comando **`goldilocks summary`** continua muito útil por consultar todos os objetos VPA rotulados pela ferramenta em todos os namespaces e consolidar as sugestões em um objeto **JSON** para automação ou relatórios; e (3) tanto `goldilocks dashboard` quanto `goldilocks summary` aceitam `--exclude-containers` com uma lista de nomes de containers separados por vírgula.

## Exemplo
```bash
# Exportar o resumo JSON de todas as recomendações VPA do cluster ocultando sidecars do Istio e Linkerd
goldilocks summary --exclude-containers=istio-proxy,linkerd-proxy,vault-agent > recomendacoes-vpa.json

# Acessar o dashboard do Goldilocks instalado no cluster via port-forward
kubectl -n goldilocks port-forward svc/goldilocks-dashboard 8080:80
```

## Limites e trade-offs
O argumento `--exclude-containers` nos comandos `dashboard` e `summary` apenas filtra a visualização e a saída JSON gerada; para impedir que o próprio VPA calcule políticas sobre um container específico no objeto `VerticalPodAutoscaler`, combine-o com `mode: "Off"` em `vpa-resource-policy`.

## Como verificar
Execute `goldilocks summary --exclude-containers=istio-proxy | jq .` e confirme que os objetos dos workloads retornam apenas as recomendações de CPU e memória dos containers de aplicação.

## Conexões
- [[goldilocks-modos-atualizacao-vpa-update-mode-resource-policy]] — Veja também: Configuração avançada de VPA no Goldilocks: vpa-update-mode e vpa-resource-policy por namespace ou workload.
- [[goldilocks-migracao-registro-imagens-imutaveis-assinadas-v4-15]] — Veja também: Migração de registro e segurança de imagens no Goldilocks (v4.15.0+): Artifact Registry, tags imutáveis e assinatura.
- [[goldilocks-dimensionamento-requests-limits-vpa-kubernetes]] — Referência cruzada direta com goldilocks-dimensionamento-requests-limits-vpa-kubernetes.

## Fontes
- [Fairwinds Goldilocks Official Documentation — Installation & Requirements (VPA Recommender, metrics-server, Helm & GKE)](https://goldilocks.docs.fairwinds.com/advanced/) — Documentação oficial de instalação do Goldilocks detalhando requisitos (VPA Recommender sem webhook, metrics-server, Prometheus opcional, GKE Standard vs Autopilot), Helm chart, manifestos e habilitação de namespaces; consultado em 2026-10-03.
- [Fairwinds Goldilocks Official Documentation — Advanced Usage & README (Controller Flags, Metrics, vpa-update-mode, vpa-resource-policy & v4.15.0+ Images)](https://goldilocks.docs.fairwinds.com/installation/) — Guia oficial de uso avançado e README do Goldilocks cobrindo flags do controlador, métricas Prometheus, anotações vpa-update-mode e vpa-resource-policy, comandos summary/dashboard, --exclude-containers e imagens assinadas v4.15.0+; consultado em 2026-10-03.
- [Fairwinds Goldilocks — Official Documentation & Repository](https://raw.githubusercontent.com/FairwindsOps/goldilocks/master/README.md) — Documentação e repositório oficial do Fairwinds Goldilocks; consultado em 2026-10-03.
