---
id: software.devops.tranche07.000641
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

# Kubescape: plataforma CNCF Incubating de segurança Kubernetes com OPA e Regolibrary

## Em uma frase
O Kubescape (projeto CNCF Incubating criado pela ARMO, sob licença Apache-2.0) é uma plataforma open-source de segurança Kubernetes que avalia clusters, manifestos YAML, Helm charts e repositórios Git contra frameworks como NSA-CISA, MITRE ATT&CK e CIS Benchmarks.

## Por que importa
Ambientes Kubernetes sofrem frequentemente com configurações inseguras em manifestos de deploy (containers rodando como root, ausência de limites de recursos, RBAC excessivamente permissivo ou falta de NetworkPolicies) que abrem brechas desde o código até a produção. Segundo o README oficial do Kubescape, a ferramenta fornece cobertura completa de segurança "shift-left to runtime", combinando gerenciamento de postura (KSPM), hardening, varredura de vulnerabilidades e segurança em tempo de execução.

## Como funciona
No modo CLI standalone, o Kubescape utiliza o motor de avaliação de políticas **Open Policy Agent (OPA)** em conjunto com a **Regolibrary** (`kubescape/regolibrary`), uma biblioteca mantida pela comunidade com centenas de controles de segurança escritos em Rego e organizados em frameworks de conformidade (`nsa`, `mitre`, `cis-v1.23-t1.0.1`, entre outros). O comando `kubescape scan` pode inspecionar um cluster ativo via `kubeconfig`, arquivos YAML locais, diretórios Kustomize, gráficos Helm ou URLs de repositórios Git, calculando pontuações de conformidade (`--compliance-threshold`) e gerando relatórios em formatos `json`, `junit`, `sarif` (para GitHub Code Scanning), `html`, `pdf` ou `csv`.

## Exemplo
```bash
# Escanear um cluster Kubernetes contra o framework NSA-CISA exigindo nota mínima de conformidade 80
kubescape scan framework nsa --compliance-threshold 80

# Escanear manifestos locais e exportar resultado em formato SARIF para CI/CD
kubescape scan ./k8s-manifests/ --format sarif --output results.sarif
```

## Limites e trade-offs
Executar `kubescape scan` diretamente em pipelines de CI sobre manifestos YAML estáticos (sem acesso ao cluster) valida excelentes práticas de segurança dos workloads, mas não consegue avaliar controles que dependem do estado vivo do control plane, da configuração de argumentos do `kube-apiserver`/`kubelet` nos nós ou de objetos RBAC já instalados no cluster; por isso, a varredura shift-left no Git deve ser complementada pela varredura in-cluster.

## Como verificar
Execute `kubescape list frameworks` e `kubescape list controls` para verificar a biblioteca de controles carregada e rode `kubescape scan` em um diretório de manifestos validando o código de saída (`0` quando acima do threshold, `1` quando abaixo).

## Conexões
- [[kubescape-varredura-vulnerabilidades-imagens-grype-multi-arch]] — Veja também: Kubescape: varredura de vulnerabilidades (CVEs) em imagens de container com Grype e inferência multi-arquitetura.
- [[kubescape-auto-remediacao-fix-manifestos-patching-copacetic]] — Referência cruzada direta com kubescape-auto-remediacao-fix-manifestos-patching-copacetic.
- [[kubescape-operador-in-cluster-monitoramento-continuo-helm]] — Referência cruzada direta com kubescape-operador-in-cluster-monitoramento-continuo-helm.

## Fontes
- [Kubescape GitHub — README.md (OPA/Regolibrary, Grype, Copacetic, VAP, Operator & MCP)](https://raw.githubusercontent.com/kubescape/kubescape/master/README.md) — README oficial do Kubescape documentando varredura de postura com OPA/Regolibrary, CVEs de imagens com Grype, auto-fix, patching com Copacetic, Validating Admission Policies (CEL) e MCP server; consultado em 2026-10-03.
- [Kubescape Official Documentation — In-Cluster Operator & Runtime Security](https://kubescape.io/docs/operator/) — Documentação oficial do operador in-cluster do Kubescape com monitoramento contínuo e detecção de ameaças em runtime via eBPF (Inspektor Gadget); consultado em 2026-10-03.
- [Kubescape — Official GitHub Repository](https://github.com/kubescape/kubescape) — Repositório oficial Apache-2.0 do Kubescape (CNCF Incubating); consultado em 2026-10-03.
