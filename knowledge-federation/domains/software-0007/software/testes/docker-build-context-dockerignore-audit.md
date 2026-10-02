---
id: software.testes.tranche08.000240
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
fontes: ["https://docs.docker.com/build/building/context/", "https://docs.docker.com/build/building/best-practices/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Docker: auditar build context e .dockerignore

## Em uma frase
Limite o build context aos arquivos necessários e exclua credenciais, caches e conteúdo irrelevante antes do build.

## Por que importa
Contexto grande aumenta tempo e pode enviar segredos ou artefatos locais ao builder sem que o Dockerfile os mencione.

## Como funciona
Revise padrões de .dockerignore junto do contexto enviado, inclua exceções deliberadas e verifique caminhos em builds locais e remotos.

## Exemplo
Diretório de aplicação contém `.env` e cache; teste do pipeline confirma que não estão no contexto e que arquivos necessários continuam acessíveis.

## Limites e trade-offs
Ignore reduz inputs do build, mas não substitui gestão de secrets nem garante que outro estágio não copie dado sensível.

## Como verificar
Inspecione contexto com comando/build progress apropriado, inclua arquivo canário sensível e confirme que ele não chega ao builder nem à imagem.

## Conexões
- [[docker-build-secrets-nao-arg-env]] — Veja também: Docker: não inserir secrets em ARG, ENV ou layers.
- [[docker-build-checks-lint-dockerfile]] — Veja também: Docker: executar build checks para detectar erros de Dockerfile.

## Fontes
- [Docker — Build context](https://docs.docker.com/build/building/context/) — arquivos incluídos/excluídos do contexto de build; consultado em 2026-10-02.
- [Docker — Building best practices](https://docs.docker.com/build/building/best-practices/) — multi-stage, pinning, cache e testes de imagens; consultado em 2026-10-02.
