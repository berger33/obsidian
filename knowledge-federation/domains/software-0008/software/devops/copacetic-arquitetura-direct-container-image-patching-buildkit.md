---
id: software.devops.tranche15.001401
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
fontes: ["https://raw.githubusercontent.com/project-copacetic/copacetic/main/README.md", "https://project-copacetic.github.io/copacetic/website/quick-start", "https://github.com/project-copacetic/copacetic"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Project Copacetic (copa): aplicação direta de patches de vulnerabilidades em imagens OCI via BuildKit

## Em uma frase
O Project Copacetic (`copa`, CNCF Sandbox, escrito em Go) aplica patches de segurança diretamente em pacotes do sistema operacional dentro de imagens de container existentes usando o BuildKit, adicionando apenas uma camada de atualização sem exigir reconstrução completa a partir do Dockerfile.

## Por que importa
A janela entre a divulgação de um CVE crítico e sua exploração ativa reduziu-se para minutos, mas corrigir vulnerabilidades herdadas de imagens base várias camadas abaixo ou de imagens de terceiros sem acesso ao código-fonte costuma exigir dias de espera pelo fornecedor upstream. O `copa` permite que engenheiros de DevSecOps corrijam a imagem imediatamente anexando uma única camada diferencial.

## Como funciona
O motor do `copa` opera em três estágios: primeiro determina o escopo de pacotes a atualizar a partir de um relatório de scanner (como Trivy) ou dos metadados de pacotes instalados na imagem alvo; em seguida invoca o gerenciador de pacotes correspondente dentro de um ambiente controlado do BuildKit para baixar e instalar apenas os binários corrigidos; por fim exporta uma nova imagem (por padrão sufixada com `-patched`) preservando os digests das camadas originais.

## Exemplo
```bash
copa patch -i docker.io/library/nginx:1.21.6 -t 1.21.6-patched
docker history docker.io/library/nginx:1.21.6-patched
```

## Limites e trade-offs
O `copa` corrige pacotes de nível de sistema operacional (como `libc`, `openssl`, `curl` gerenciados por `apt`, `apk`, `yum`/`dnf`, `tdnf` ou `chisel`), mas não atualiza dependências de linguagem compiladas dentro do binário da aplicação (como módulos Go ou jars Java), que continuam exigindo rebuild da aplicação.

## Como verificar
Compare `docker history` da imagem original e da imagem `-patched` e confirme que todos os digests das camadas base permanecem idênticos, com apenas uma camada adicional de patch no topo.

## Conexões
- [[copacetic-targeted-patching-relatorios-trivy-vuln-type-os]] — Veja também: Project Copacetic: patching direcionado (Targeted Patching) guiado por relatórios JSON do Trivy.

## Fontes
- [Project Copacetic GitHub — README.md (Direct Container Image Patching, BuildKit Engine, Ubuntu Chiseled Images & Extensible Adapters)](https://raw.githubusercontent.com/project-copacetic/copacetic/main/README.md) — README oficial do project-copacetic/copacetic (CNCF Sandbox) detalhando a arquitetura de patching direto sem rebuild, suporte a Ubuntu Chiseled e integração com scanners; consultado em 2026-10-03.
- [Project Copacetic Official Documentation — Quick Start (Targeted vs Comprehensive Patching, Trivy Reports, BuildKit Auto-Detection & Compression)](https://project-copacetic.github.io/copacetic/website/quick-start) — Guia oficial Quick Start do Copacetic demonstrando o fluxo completo de scan com Trivy, patching direcionado (-r) vs abrangente, controle de compressão e verificação; consultado em 2026-10-03.
- [Project Copacetic — Official GitHub Repository](https://github.com/project-copacetic/copacetic) — Repositório oficial Apache-2.0 do Project Copacetic na CNCF; consultado em 2026-10-03.
