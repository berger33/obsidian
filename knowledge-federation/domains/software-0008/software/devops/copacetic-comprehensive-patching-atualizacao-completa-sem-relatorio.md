---
id: software.devops.tranche15.001403
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

# Project Copacetic: patching abrangente (Comprehensive Patching) sem relatório de scanner

## Em uma frase
Quando executado sem a flag `-r`/`--report` (`copa patch -i <imagem>`), o Copacetic realiza um patching abrangente que atualiza todos os pacotes desatualizados do sistema operacional para suas versões mais recentes disponíveis nos repositórios da distribuição.

## Por que importa
Em imagens onde o scanner de vulnerabilidades ainda não catalogou determinado CVE recém-corrigido pela distribuição ou em imagens Ubuntu Chiseled nativas baseadas em `manifest.wall`, o patching abrangente garante que todo o conjunto de pacotes instalados receba as últimas correções do repositório oficial.

## Como funciona
Sem um relatório externo, o Copacetic inspeciona diretamente o banco de metadados de pacotes dentro da imagem alvo (por exemplo `/var/lib/dpkg/status`, `/lib/apk/db/installed` ou `/var/lib/rpm`) e executa uma atualização completa não interativa equivalente a `apt-get upgrade` ou `apk upgrade` dentro do solver do BuildKit.

## Exemplo
```bash
copa patch -i docker.io/library/nginx:1.21.6 -t 1.21.6-comprehensive --timeout 10m
docker run --rm docker.io/library/nginx:1.21.6-comprehensive nginx -v
```

## Limites e trade-offs
Como o patching abrangente atualiza pacotes que não estavam necessariamente listados em um boletim de segurança específico, o risco de incompatibilidade de ABI ou mudança comportamental é maior do que no modo direcionado, exigindo bateria completa de smoke tests antes do deploy.

## Como verificar
Inicie um container de teste com a imagem atualizada (`docker run -d -p 8080:80`) e valide tanto a resposta HTTP da aplicação quanto a ausência de pacotes pendentes de upgrade no gerenciador da distro.

## Conexões
- [[copacetic-targeted-patching-relatorios-trivy-vuln-type-os]] — Veja também: Project Copacetic: patching direcionado (Targeted Patching) guiado por relatórios JSON do Trivy.
- [[copacetic-ubuntu-chiseled-images-dpkg-status-vs-manifest-wall]] — Veja também: Project Copacetic: aplicação de patches em imagens Ubuntu Chiseled (`dpkg/status` vs `manifest.wall`).

## Fontes
- [Project Copacetic GitHub — README.md (Direct Container Image Patching, BuildKit Engine, Ubuntu Chiseled Images & Extensible Adapters)](https://project-copacetic.github.io/copacetic/website/quick-start) — README oficial do project-copacetic/copacetic (CNCF Sandbox) detalhando a arquitetura de patching direto sem rebuild, suporte a Ubuntu Chiseled e integração com scanners; consultado em 2026-10-03.
- [Project Copacetic Official Documentation — Quick Start (Targeted vs Comprehensive Patching, Trivy Reports, BuildKit Auto-Detection & Compression)](https://raw.githubusercontent.com/project-copacetic/copacetic/main/README.md) — Guia oficial Quick Start do Copacetic demonstrando o fluxo completo de scan com Trivy, patching direcionado (-r) vs abrangente, controle de compressão e verificação; consultado em 2026-10-03.
- [Project Copacetic — Official GitHub Repository](https://github.com/project-copacetic/copacetic) — Repositório oficial Apache-2.0 do Project Copacetic na CNCF; consultado em 2026-10-03.
