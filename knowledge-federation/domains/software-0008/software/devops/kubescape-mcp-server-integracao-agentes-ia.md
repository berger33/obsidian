---
id: software.devops.tranche07.000648
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

# Kubescape: servidor MCP (Model Context Protocol) para consulta de vulnerabilidades e postura via agentes de IA

## Em uma frase
O subcomando `kubescape mcpserver` inicia um servidor Model Context Protocol (MCP) que expõe os manifestos de vulnerabilidades (CVEs) e de varredura de configuração do cluster para assistentes de IA.

## Por que importa
Em clusters com centenas de microsserviços, cruzar manualmente relatórios de configuração e listas de CVEs para responder perguntas como "quais deployments em produção possuem vulnerabilidades críticas com correção disponível e também rodam como root?" exige escrever múltiplos scripts `jq` sobre CRDs extensos. Segundo o README oficial do Kubescape, o servidor MCP integrado permite que assistentes de IA consultem diretamente a postura de segurança do cluster em linguagem natural usando ferramentas padronizadas.

## Como funciona
Quando executado com `kubescape mcpserver`, o binário do Kubescape conecta-se ao cluster Kubernetes onde o Kubescape Operator armazena seus relatórios de segurança e expõe cinco ferramentas MCP estruturadas para clientes compatíveis: `list_vulnerability_manifests` (descobre os manifestos de vulnerabilidade disponíveis), `list_vulnerabilities_in_manifest` (lista os CVEs contidos em um manifesto específico), `list_vulnerability_matches_for_cve` (obtém detalhes completos das ocorrências de um CVE específico), `list_configuration_security_scan_manifests` (lista os resultados de varreduras de segurança de configuração) e `get_configuration_security_scan_manifest` (retorna os detalhes de conformidade e controles falhos de um manifesto específico).

## Exemplo
```bash
# Iniciar o servidor MCP do Kubescape para integração com assistentes de IA
kubescape mcpserver
```

## Limites e trade-offs
O servidor MCP do Kubescape lê os recursos customizados gerados pelo Kubescape Operator dentro do cluster usando as credenciais do `kubeconfig` local; portanto, ele requer que o operador in-cluster esteja instalado e com as varreduras de vulnerabilidades e configuração habilitadas, e o acesso ao `mcpserver` deve ser restrito a operadores autorizados, pois expõe o inventário completo de vulnerabilidades exploráveis do ambiente.

## Como verificar
Com o `kubescape-operator` ativo no cluster, inicie `kubescape mcpserver` em um cliente MCP e invoque a ferramenta `list_configuration_security_scan_manifests` para confirmar o retorno dos manifestos de scan do cluster.

## Conexões
- [[kubescape-execucao-offline-air-gapped-protecao-metadados]] — Veja também: Kubescape: operação offline/air-gapped (kubescape download) e proteção de metadados com pseudonimização e criptografia.
- [[kubescape-integracao-cicd-github-actions-gitlab-megalinter-sarif]] — Veja também: Kubescape: integração em pipelines CI/CD com GitHub Actions, GitLab CI, Jenkins, MegaLinter e relatórios SARIF/JUnit.
- [[kubescape-plataforma-seguranca-kubernetes-opa-regolibrary]] — Referência cruzada direta com kubescape-plataforma-seguranca-kubernetes-opa-regolibrary.
- [[kubescape-operador-in-cluster-monitoramento-continuo-helm]] — Referência cruzada direta com kubescape-operador-in-cluster-monitoramento-continuo-helm.
- [[opencost-mcp-server-agentes-ia-ferramentas-custos]] — Referência cruzada direta com opencost-mcp-server-agentes-ia-ferramentas-custos.

## Fontes
- [Kubescape GitHub — README.md (OPA/Regolibrary, Grype, Copacetic, VAP, Operator & MCP)](https://raw.githubusercontent.com/kubescape/kubescape/master/README.md) — README oficial do Kubescape documentando varredura de postura com OPA/Regolibrary, CVEs de imagens com Grype, auto-fix, patching com Copacetic, Validating Admission Policies (CEL) e MCP server; consultado em 2026-10-03.
- [Kubescape Official Documentation — In-Cluster Operator & Runtime Security](https://kubescape.io/docs/operator/) — Documentação oficial do operador in-cluster do Kubescape com monitoramento contínuo e detecção de ameaças em runtime via eBPF (Inspektor Gadget); consultado em 2026-10-03.
- [Kubescape — Official GitHub Repository](https://github.com/kubescape/kubescape) — Repositório oficial Apache-2.0 do Kubescape (CNCF Incubating); consultado em 2026-10-03.
