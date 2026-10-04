---
id: software.testes.tranche08.000241
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
fontes: ["https://docs.docker.com/build/building/multi-stage/", "https://docs.docker.com/build/building/best-practices/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Docker: verificar fronteira entre build stage e runtime

## Em uma frase
Use multi-stage build para separar ferramentas de compilação do conjunto mínimo de runtime quando isso servir ao produto.

## Por que importa
Imagem final menor pode reduzir superfície e transferência, enquanto estágio de build mantém compiladores e dependências necessárias à compilação.

## Como funciona
Copie apenas artefatos requeridos para o estágio final e teste entrypoint e arquivos necessários em container produzido.

## Exemplo
Builder compila aplicação e runtime recebe binário e certificados necessários; teste inicia imagem final sem depender de diretório do builder.

## Limites e trade-offs
Imagem menor não garante segurança ou compatibilidade; remoção de shell ou bibliotecas pode quebrar diagnóstico e requisito de runtime.

## Como verificar
Inspecione layers e conteúdo final, execute smoke test com usuário e ambiente reais e confirme que artefato foi copiado do estágio esperado.

## Conexões
- [[docker-image-test-smoke-entrypoint]] — Veja também: Docker: testar a imagem final com smoke test.
- [[docker-container-nonroot-permissions]] — Veja também: Docker: testar execução com usuário não privilegiado.

## Fontes
- [Docker — Multi-stage builds](https://docs.docker.com/build/building/multi-stage/) — separação entre compilação e imagem runtime; consultado em 2026-10-02.
- [Docker — Building best practices](https://docs.docker.com/build/building/best-practices/) — multi-stage, pinning, cache e testes de imagens; consultado em 2026-10-02.
