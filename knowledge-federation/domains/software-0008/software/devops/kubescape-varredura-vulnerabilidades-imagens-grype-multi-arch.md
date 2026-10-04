---
id: software.devops.tranche07.000642
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

# Kubescape: varredura de vulnerabilidades (CVEs) em imagens de container com Grype e inferência multi-arquitetura

## Em uma frase
O subcomando `kubescape scan image` integra o motor Anchore Grype para detectar CVEs em imagens de container públicas ou privadas, com suporte a banco de vulnerabilidades offline e inferência de plataforma multi-arquitetura.

## Por que importa
Um manifesto Kubernetes perfeitamente endurecido (non-root, read-only root filesystem) ainda pode ser comprometido se a imagem de container que ele executa contiver bibliotecas de sistema ou pacotes de linguagem com vulnerabilidades críticas conhecidas (CVEs). De acordo com o README oficial do Kubescape, unificar a análise de configuração do Kubernetes e a varredura de vulnerabilidades de imagens via Grype em uma única ferramenta simplifica a governança de segurança no CI/CD e no cluster.

## Como funciona
Ao executar `kubescape scan image <imagem>`, o Kubescape utiliza internamente o scanner **Grype** para inspecionar as camadas da imagem OCI e cruzar os pacotes instalados com o banco de dados de CVEs. Para imagens multi-arquitetura (image index), pode-se especificar explicitamente a variante com `--platform linux/amd64` ou `linux/arm64`; além disso, durante varreduras de workloads no cluster com `--scan-images`, o Kubescape consegue inferir automaticamente a plataforma da imagem a partir dos nós onde os pods estão agendados, `nodeSelector` e `nodeAffinity` (permitindo sobrescrever com `--image-platform`). Em ambientes air-gapped, o scanner pode apontar para um container local do banco Grype via `--grype-db-url`.

## Exemplo
```bash
# Escanear uma variante específica de arquitetura de uma imagem de container com saída detalhada
kubescape scan image nginx:1.27 --platform linux/amd64 -v

# Escanear usando um banco de dados Grype offline rodando localmente na porta 8080
docker run -d --rm -p 8080:8080 quay.io/kubescape/grype-offline-db:v6-latest
kubescape scan image --grype-db-url http://localhost:8080/databases/ nginx:latest
```

## Limites e trade-offs
Habilitar a varredura de imagens de todos os workloads durante um `kubescape scan` de cluster completo exige baixar e descompactar as camadas de cada imagem referenciada pelos pods, o que aumenta substancialmente o tempo de execução, o tráfego de rede e o uso de disco temporário em comparação com uma varredura puramente de manifestos YAML.

## Como verificar
Execute `kubescape scan image nginx:1.21` e confirme a exibição da tabela de vulnerabilidades encontradas agrupadas por severidade (`Critical`, `High`, `Medium`, `Low`) e disponibilidade de versão corrigida (`Fixed in`).

## Conexões
- [[kubescape-plataforma-seguranca-kubernetes-opa-regolibrary]] — Veja também: Kubescape: plataforma CNCF Incubating de segurança Kubernetes com OPA e Regolibrary.
- [[kubescape-auto-remediacao-fix-manifestos-patching-copacetic]] — Veja também: Kubescape: auto-remediação de manifestos (kubescape fix) e patching de imagens com Copacetic (kubescape patch).
- [[kubescape-execucao-offline-air-gapped-protecao-metadados]] — Referência cruzada direta com kubescape-execucao-offline-air-gapped-protecao-metadados.

## Fontes
- [Kubescape GitHub — README.md (OPA/Regolibrary, Grype, Copacetic, VAP, Operator & MCP)](https://raw.githubusercontent.com/kubescape/kubescape/master/README.md) — README oficial do Kubescape documentando varredura de postura com OPA/Regolibrary, CVEs de imagens com Grype, auto-fix, patching com Copacetic, Validating Admission Policies (CEL) e MCP server; consultado em 2026-10-03.
- [Kubescape Official Documentation — In-Cluster Operator & Runtime Security](https://kubescape.io/docs/operator/) — Documentação oficial do operador in-cluster do Kubescape com monitoramento contínuo e detecção de ameaças em runtime via eBPF (Inspektor Gadget); consultado em 2026-10-03.
- [Kubescape — Official GitHub Repository](https://github.com/kubescape/kubescape) — Repositório oficial Apache-2.0 do Kubescape (CNCF Incubating); consultado em 2026-10-03.
