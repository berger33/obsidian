---
id: software.testes.tranche08.000245
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-08.md"
fontes: ["https://docs.docker.com/build/building/best-practices/", "https://docs.docker.com/build/building/multi-stage/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Docker: testar execução com usuário não privilegiado

## Em uma frase
Execute a imagem final com identidade sem privilégios quando compatível com a aplicação e valide permissões necessárias.

## Por que importa
Build bem-sucedido não revela que processo pode escrever em caminho indevido ou que precisa de root para iniciar.

## Como funciona
Configure usuário no estágio final, monte diretórios com ownership mínimo e teste portas, arquivos e sinais no modo de execução real.

## Exemplo
Container inicia como UID não-root, grava apenas em diretório temporário permitido e falha claramente se tentar alterar arquivo da aplicação.

## Limites e trade-offs
UID não-root reduz privilégio, mas não substitui isolamento do host, capabilities restritas, seccomp ou configuração do runtime.

## Como verificar
Inspecione usuário efetivo, tente escrita em caminho protegido e execute smoke test com volume e política de produção.

## Conexões
- [[docker-multistage-runtime-minimo]] — Veja também: Docker: verificar fronteira entre build stage e runtime.
- [[docker-runtime-healthcheck-supervision]] — Veja também: Docker: validar healthcheck sem confundi-lo com readiness.

## Fontes
- [Docker — Building best practices](https://docs.docker.com/build/building/best-practices/) — multi-stage, pinning, cache e testes de imagens; consultado em 2026-10-02.
- [Docker — Multi-stage builds](https://docs.docker.com/build/building/multi-stage/) — separação entre compilação e imagem runtime; consultado em 2026-10-02.
