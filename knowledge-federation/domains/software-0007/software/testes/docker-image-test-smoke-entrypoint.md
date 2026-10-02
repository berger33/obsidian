---
id: software.testes.tranche08.000247
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

# Docker: testar a imagem final com smoke test

## Em uma frase
Execute a imagem resultante em ambiente descartável e valide entrypoint, configuração e endpoint essencial após o build.

## Por que importa
Teste de código não detecta arquivo ausente, permissão incorreta ou dependência que ficou fora da camada runtime.

## Como funciona
Rode container com parâmetros próximos do deploy, teste inicialização e encerramento e capture logs sem incluir credenciais.

## Exemplo
Pipeline cria imagem e verifica resposta de health endpoint e shutdown limpo antes de publicar tag.

## Limites e trade-offs
Smoke test cobre caminho curto e não prova carga, disponibilidade prolongada ou compatibilidade com toda configuração de produção.

## Como verificar
Use imagem construída, não substituta local; valide exit code, endpoint, sinais e ausência de dependência do workspace do builder.

## Conexões
- [[docker-multistage-runtime-minimo]] — Veja também: Docker: verificar fronteira entre build stage e runtime.
- [[docker-build-checks-lint-dockerfile]] — Veja também: Docker: executar build checks para detectar erros de Dockerfile.

## Fontes
- [Docker — Building best practices](https://docs.docker.com/build/building/best-practices/) — multi-stage, pinning, cache e testes de imagens; consultado em 2026-10-02.
- [Docker — Multi-stage builds](https://docs.docker.com/build/building/multi-stage/) — separação entre compilação e imagem runtime; consultado em 2026-10-02.
