---
id: software.devops.tranche15.001402
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

# Project Copacetic: patching direcionado (Targeted Patching) guiado por relatórios JSON do Trivy

## Em uma frase
Na estratégia de patching direcionado (`copa patch -r report.json`), o Copacetic atualiza exclusivamente os pacotes do sistema operacional apontados como vulneráveis e com correção disponível por um scanner como o Trivy.

## Por que importa
Atualizar cegamente todos os pacotes de uma imagem em produção pode introduzir regressões sutis em bibliotecas que não tinham vulnerabilidades de segurança. Ao restringir o patch exatamente aos pacotes listados no relatório JSON do scanner, a superfície de mudança é minimizada ao estritamente necessário para cumprir o SLA de segurança.

## Como funciona
O operador executa `trivy image --vuln-type os --ignore-unfixed -f json -o report.json <imagem>` para gerar o inventário estruturado de CVEs de SO corrigíveis. Ao passar `-r report.json` para `copa patch`, o adaptador de relatório do Copacetic extrai os nomes dos pacotes e versões corrigidas (`FixedVersion`) e instrui o BuildKit a atualizar somente esses pacotes na camada de patch.

## Exemplo
```bash
export IMAGE=docker.io/library/nginx:1.21.6
trivy image --vuln-type os --ignore-unfixed -f json -o nginx-report.json $IMAGE
copa patch -r nginx-report.json -i $IMAGE -t 1.21.6-patched
trivy image --vuln-type os --ignore-unfixed docker.io/library/nginx:1.21.6-patched
```

## Limites e trade-offs
A flag `--ignore-unfixed` deve ser usada ao gerar o relatório para o Trivy, pois vulnerabilidades sem correção publicada pela distribuição Linux não podem ser resolvidas via gerenciador de pacotes e causariam avisos ou falhas desnecessárias no fluxo.

## Como verificar
Execute o comando `trivy image --vuln-type os --ignore-unfixed` contra a imagem resultante `:1.21.6-patched` e valide que o total de vulnerabilidades críticas e altas corrigíveis caiu para `0`.

## Conexões
- [[copacetic-arquitetura-direct-container-image-patching-buildkit]] — Veja também: Project Copacetic (copa): aplicação direta de patches de vulnerabilidades em imagens OCI via BuildKit.
- [[copacetic-comprehensive-patching-atualizacao-completa-sem-relatorio]] — Veja também: Project Copacetic: patching abrangente (Comprehensive Patching) sem relatório de scanner.

## Fontes
- [Project Copacetic GitHub — README.md (Direct Container Image Patching, BuildKit Engine, Ubuntu Chiseled Images & Extensible Adapters)](https://project-copacetic.github.io/copacetic/website/quick-start) — README oficial do project-copacetic/copacetic (CNCF Sandbox) detalhando a arquitetura de patching direto sem rebuild, suporte a Ubuntu Chiseled e integração com scanners; consultado em 2026-10-03.
- [Project Copacetic Official Documentation — Quick Start (Targeted vs Comprehensive Patching, Trivy Reports, BuildKit Auto-Detection & Compression)](https://raw.githubusercontent.com/project-copacetic/copacetic/main/README.md) — Guia oficial Quick Start do Copacetic demonstrando o fluxo completo de scan com Trivy, patching direcionado (-r) vs abrangente, controle de compressão e verificação; consultado em 2026-10-03.
- [Project Copacetic — Official GitHub Repository](https://github.com/project-copacetic/copacetic) — Repositório oficial Apache-2.0 do Project Copacetic na CNCF; consultado em 2026-10-03.
