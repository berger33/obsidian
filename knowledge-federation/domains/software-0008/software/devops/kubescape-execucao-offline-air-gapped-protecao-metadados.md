---
id: software.devops.tranche07.000647
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

# Kubescape: operação offline/air-gapped (kubescape download) e proteção de metadados com pseudonimização e criptografia

## Em uma frase
O Kubescape suporta ambientes totalmente desconectados via `kubescape download artifacts` / `--use-artifacts-from` e protege dados sensíveis de relatórios com pseudonimização determinística (`--hide`) ou criptografia (`--encrypt` / `kubescape decrypt`).

## Por que importa
Clusters Kubernetes em setores financeiro, governamental, defesa e telecomunicações frequentemente operam em redes air-gapped sem acesso à internet para baixar a Regolibrary, e suas políticas de segurança da informação proíbem exportar relatórios JSON contendo nomes reais de namespaces, workloads e contas internas sem anonimização ou criptografia. O README oficial do Kubescape documenta comandos nativos tanto para operação offline quanto para proteção de metadados de relatórios.

## Como funciona
Para operação offline, o engenheiro executa em uma máquina conectada `kubescape download artifacts --output /caminho/offline` (ou `kubescape download framework nsa --output nsa.json`) para salvar localmente todos os frameworks e controles Rego, e depois executa a varredura no ambiente isolado passando `kubescape scan --use-artifacts-from /caminho/offline`. Para proteção de metadados em relatórios, a flag `--hide` aplica pseudonimização determinística aos identificadores sensíveis do cluster na saída, enquanto a flag `--encrypt` (usada com a variável de ambiente `KUBESCAPE_MASTER_KEY` contendo uma passphrase de pelo menos 16 caracteres) criptografa os metadados sensíveis dentro do relatório JSON, permitindo descriptografá-los posteriormente de forma autorizada com `kubescape decrypt encrypted-report.json`.

## Exemplo
```bash
# Baixar artefatos de controles e frameworks para uso em ambiente air-gapped
kubescape download artifacts --output ./kubescape-offline-artifacts
kubescape scan --use-artifacts-from ./kubescape-offline-artifacts

# Gerar relatório JSON com metadados sensíveis criptografados e descriptografar
export KUBESCAPE_MASTER_KEY="minha-chave-mestra-segura-2026"
kubescape scan --encrypt --format json --output encrypted-report.json
kubescape decrypt encrypted-report.json > decrypted-report.json
```

## Limites e trade-offs
Ao utilizar `--use-artifacts-from` em ambientes air-gapped, os controles de segurança avaliados ficam congelados na versão dos artefatos baixados; a equipe de segurança precisa estabelecer uma rotina periódica para atualizar o pacote de artefatos da Regolibrary e a imagem `quay.io/kubescape/grype-offline-db` para não ficar cega a novos controles do Kubernetes e novos CVEs.

## Como verificar
Execute `kubescape scan --hide --format json --output hidden.json` e inspecione o arquivo gerado para confirmar que os nomes reais dos recursos foram pseudonimizados de forma consistente.

## Conexões
- [[kubescape-monitoramento-runtime-ebpf-network-policies-prometheus]] — Veja também: Kubescape: detecção de ameaças em runtime com eBPF (Inspektor Gadget) e geração de NetworkPolicies.
- [[kubescape-mcp-server-integracao-agentes-ia]] — Veja também: Kubescape: servidor MCP (Model Context Protocol) para consulta de vulnerabilidades e postura via agentes de IA.
- [[kubescape-plataforma-seguranca-kubernetes-opa-regolibrary]] — Referência cruzada direta com kubescape-plataforma-seguranca-kubernetes-opa-regolibrary.
- [[kubescape-varredura-vulnerabilidades-imagens-grype-multi-arch]] — Referência cruzada direta com kubescape-varredura-vulnerabilidades-imagens-grype-multi-arch.

## Fontes
- [Kubescape GitHub — README.md (OPA/Regolibrary, Grype, Copacetic, VAP, Operator & MCP)](https://raw.githubusercontent.com/kubescape/kubescape/master/README.md) — README oficial do Kubescape documentando varredura de postura com OPA/Regolibrary, CVEs de imagens com Grype, auto-fix, patching com Copacetic, Validating Admission Policies (CEL) e MCP server; consultado em 2026-10-03.
- [Kubescape Official Documentation — In-Cluster Operator & Runtime Security](https://kubescape.io/docs/operator/) — Documentação oficial do operador in-cluster do Kubescape com monitoramento contínuo e detecção de ameaças em runtime via eBPF (Inspektor Gadget); consultado em 2026-10-03.
- [Kubescape — Official GitHub Repository](https://github.com/kubescape/kubescape) — Repositório oficial Apache-2.0 do Kubescape (CNCF Incubating); consultado em 2026-10-03.
