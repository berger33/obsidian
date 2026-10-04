---
id: software.devops.tranche07.000649
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-07.md"
fontes: ["https://raw.githubusercontent.com/kubescape/kubescape/master/README.md", "https://kubescape.io/docs/operator/", "https://github.com/kubescape/kubescape"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Kubescape: integração em pipelines CI/CD com GitHub Actions, GitLab CI, Jenkins, MegaLinter e relatórios SARIF/JUnit

## Em uma frase
O Kubescape integra-se a pipelines de CI/CD (GitHub Actions, GitLab CI, Jenkins e MegaLinter) utilizando limites de conformidade (`--compliance-threshold`) e severidade (`--severity-threshold`) com exportação em SARIF e JUnit XML.

## Por que importa
Detectar que um manifesto Kubernetes ou Helm chart viola controles críticos do framework NSA-CISA ou MITRE apenas depois que ele foi aplicado em produção gera retrabalho e janelas de exposição desnecessárias. De acordo com o README oficial do Kubescape, embutir a validação diretamente nos pull requests (inclusive por meio de agregadores como o MegaLinter, que aciona o Kubescape automaticamente ao detectar arquivos Kubernetes) garante segurança shift-left contínua.

## Como funciona
Nos pipelines de integração contínua, a CLI `kubescape scan` avalia os arquivos YAML, diretórios Kustomize ou gráficos Helm modificados no repositório. O engenheiro de DevOps configura gates de aprovação usando `--compliance-threshold <0-100>` (que força código de saída `1` caso a pontuação do framework/controle ou da visão `--view resource|control` fique abaixo do mínimo exigido) ou `--severity-threshold <low|medium|high|critical>` (que falha o job se qualquer controle violado atingir a severidade especificada). Os resultados são gerados com `--format sarif --output results.sarif` para alimentar a aba Security / Code Scanning do GitHub ou `--format junit --output results.xml` para relatórios nativos de testes no GitLab CI e Jenkins.

## Exemplo
```bash
# Comando de gate em pipeline CI/CD escaneando um Helm chart com threshold de severidade alta e saída JUnit
kubescape scan ./charts/meu-servico/ \
  --severity-threshold high \
  --format junit \
  --output kubescape-junit.xml
```

## Limites e trade-offs
Definir `--severity-threshold medium` ou `--compliance-threshold 95` imediatamente em um repositório legado com dezenas de manifestos antigos bloqueará todos os deploys da equipe; a adoção eficaz em CI/CD recomenda começar com `--severity-threshold critical` (ou escaneando controles específicos com `kubescape scan control C-0005`), usar `kubescape fix` para sanear o passivo e elevar o threshold progressivamente.

## Como verificar
Execute o comando `kubescape scan` com `--compliance-threshold 100` sobre um manifesto de teste sem limites de recursos e confirme que o processo retorna código de saída não-zero (`echo $?` igual a `1`) e gera o arquivo `.sarif` ou `.xml`.

## Conexões
- [[kubescape-mcp-server-integracao-agentes-ia]] — Veja também: Kubescape: servidor MCP (Model Context Protocol) para consulta de vulnerabilidades e postura via agentes de IA.
- [[kubescape-filtros-escopo-namespaces-controles-config-cache]] — Veja também: Kubescape: filtragem de escopo por namespaces, execução de controles individuais e gerenciamento de cache.
- [[kubescape-plataforma-seguranca-kubernetes-opa-regolibrary]] — Referência cruzada direta com kubescape-plataforma-seguranca-kubernetes-opa-regolibrary.
- [[kubescape-auto-remediacao-fix-manifestos-patching-copacetic]] — Referência cruzada direta com kubescape-auto-remediacao-fix-manifestos-patching-copacetic.

## Fontes
- [Kubescape GitHub — README.md (OPA/Regolibrary, Grype, Copacetic, VAP, Operator & MCP)](https://raw.githubusercontent.com/kubescape/kubescape/master/README.md) — README oficial do Kubescape documentando varredura de postura com OPA/Regolibrary, CVEs de imagens com Grype, auto-fix, patching com Copacetic, Validating Admission Policies (CEL) e MCP server; consultado em 2026-10-03.
- [Kubescape Official Documentation — In-Cluster Operator & Runtime Security](https://kubescape.io/docs/operator/) — Documentação oficial do operador in-cluster do Kubescape com monitoramento contínuo e detecção de ameaças em runtime via eBPF (Inspektor Gadget); consultado em 2026-10-03.
- [Kubescape — Official GitHub Repository](https://github.com/kubescape/kubescape) — Repositório oficial Apache-2.0 do Kubescape (CNCF Incubating); consultado em 2026-10-03.
