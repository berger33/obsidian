---
id: software.devops.tranche14.001328
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-14.md"
fontes: ["https://raw.githubusercontent.com/kubernetes-sigs/headlamp/main/README.md", "https://headlamp.dev/docs/latest/installation/in-cluster/", "https://github.com/kubernetes-sigs/headlamp"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Headlamp: Desenvolvimento de Plugins Customizados para Plataformas Internas (IDPs)

## Em uma frase
O Headlamp oferece um SDK de desenvolvimento de plugins (`@kinvolk/headlamp-plugin`) em TypeScript/React que permite a equipes de engenharia de plataforma customizar a barra lateral, adicionar novas páginas para CRDs internas (como Promises do Kratix, Compositions do Crossplane ou Argo Rollouts) e alterar temas.

## Por que importa
Construir do zero um portal web próprio apenas para exibir o status de 3 ou 4 CRDs internas da plataforma exige manter autenticação Kubernetes, WebSockets e tabelas complexas.

## Como funciona
Com o gerador de plugins do Headlamp, a equipe cria um pacote modular que registra componentes visuais nos pontos de extensão da UI (como botões de cabeçalho, abas de detalhes de Pod/Namespace ou rotas dedicadas) e o empacota para carregamento pelo `pluginsManager`.

## Exemplo
```bash
npx @kinvolk/headlamp-plugin create my-platform-plugin
cd my-platform-plugin
npm test
npm run build
```

## Limites e trade-offs
Fazer chamadas diretas a APIs externas sem passar pelo proxy/contexto autenticado do cluster no plugin pode falhar por políticas de CORS no navegador.

## Como verificar
Utilize as APIs fornecidas pelo SDK `@kinvolk/headlamp-plugin` (`K8s.ResourceClasses`, `ApiProxy`) para consultar recursos e CRDs do cluster com o contexto do usuário.

## Conexões
- [[headlamp-operacoes-interativas-logs-exec-editor-cancelavel]] — Veja também: Headlamp: Operações Interativas de Logs, Terminal Exec, Editor com Documentação e Ações Canceláveis.
- [[headlamp-implantacao-simples-manifesto-vanilla-vs-helm-ha]] — Veja também: Headlamp: Implantação Vanilla (kubernetes-headlamp.yaml) vs Alta Disponibilidade via Helm Chart.

## Fontes
- [Headlamp GitHub — README.md (Kubernetes SIG UI Web & Desktop App, RBAC-Aware Controls, Multi-Cluster & Plugins)](https://raw.githubusercontent.com/kubernetes-sigs/headlamp/main/README.md) — README oficial do kubernetes-sigs/headlamp (Apache-2.0) detalhando funcionalidades multi-cluster, reflexão de permissões RBAC na UI, terminal/logs/editor e ecossistema de plugins no Artifact Hub; consultado em 2026-10-03.
- [Headlamp Official Documentation — In-Cluster Installation (Helm Chart, Cluster Inventory API, Multiple Kubeconfigs, TLS, OIDC & pluginsManager Sidecar)](https://headlamp.dev/docs/latest/installation/in-cluster/) — Guia oficial de implantação in-cluster do Headlamp cobrindo Helm chart, descoberta via ClusterProfile/secretreader, variáveis KUBECONFIG e sidecar pluginsManager; consultado em 2026-10-03.
- [Headlamp — Official GitHub Repository](https://github.com/kubernetes-sigs/headlamp) — Repositório oficial do Headlamp no Kubernetes SIG UI; consultado em 2026-10-03.
