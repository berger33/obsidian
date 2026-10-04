---
id: software.devops.tranche15.001410
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-15.md"
fontes: ["https://project-copacetic.github.io/copacetic/website/quick-start", "https://raw.githubusercontent.com/project-copacetic/copacetic/main/README.md", "https://github.com/project-copacetic/copacetic"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Project Copacetic: integração em pipelines DevSecOps com Trivy, Cosign, Notation e Kubescape

## Em uma frase
O Copacetic integra-se nativamente em esteiras de resposta contínua a vulnerabilidades, onde imagens em produção escaneadas por Trivy ou Kubescape são corrigidas via `copa patch`, re-escaneadas, assinadas com Cosign ou Notation e promovidas via GitOps.

## Por que importa
Permite automatizar o *hot-patching* de imagens de terceiros (como ingress controllers, exporters ou bancos de dados) cujos mantenedores upstream ainda não publicaram uma nova release para corrigir CVEs de bibliotecas base do sistema operacional.

## Como funciona
O pipeline executa o scan inicial com Trivy, invoca `copa patch` se o número de CVEs corrigíveis for maior que zero, executa o gate de verificação com um segundo scan Trivy mais um smoke test em container efêmero, publica a imagem corrigida no registry interno e anexa a assinatura criptográfica e o novo SBOM.

## Exemplo
```bash
IMAGE="docker.io/library/nginx:1.21.6"
trivy image --vuln-type os --ignore-unfixed --exit-code 0 -f json -o report.json "$IMAGE"
copa patch -i "$IMAGE" -r report.json -t "1.21.6-patched"
trivy image --vuln-type os --ignore-unfixed --exit-code 1 "docker.io/library/nginx:1.21.6-patched"
```

## Limites e trade-offs
Como o `copa` gera um novo manifesto OCI com um novo digest SHA-256, qualquer assinatura Cosign ou Notation anterior da imagem original deixa de valer para a imagem `-patched`, tornando obrigatório re-assinar o artefato corrigido no pipeline interno.

## Como verificar
Confirme que o segundo comando `trivy image --exit-code 1` retorna código de saída `0` antes de publicar e assinar a imagem corrigida no registry corporativo.

## Conexões
- [[copacetic-economia-armazenamento-rede-camada-diferencial-cache]] — Veja também: Project Copacetic: redução de custos de armazenamento, tráfego de rede e tempo de resposta a incidentes.

## Fontes
- [Project Copacetic GitHub — README.md (Direct Container Image Patching, BuildKit Engine, Ubuntu Chiseled Images & Extensible Adapters)](https://project-copacetic.github.io/copacetic/website/quick-start) — README oficial do project-copacetic/copacetic (CNCF Sandbox) detalhando a arquitetura de patching direto sem rebuild, suporte a Ubuntu Chiseled e integração com scanners; consultado em 2026-10-03.
- [Project Copacetic Official Documentation — Quick Start (Targeted vs Comprehensive Patching, Trivy Reports, BuildKit Auto-Detection & Compression)](https://raw.githubusercontent.com/project-copacetic/copacetic/main/README.md) — Guia oficial Quick Start do Copacetic demonstrando o fluxo completo de scan com Trivy, patching direcionado (-r) vs abrangente, controle de compressão e verificação; consultado em 2026-10-03.
- [Project Copacetic — Official GitHub Repository](https://github.com/project-copacetic/copacetic) — Repositório oficial Apache-2.0 do Project Copacetic na CNCF; consultado em 2026-10-03.
