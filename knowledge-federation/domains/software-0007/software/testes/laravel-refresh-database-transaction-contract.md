---
id: software.testes.tranche14.000832
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-14.md"
fontes: ["https://laravel.com/framework/docs/13.x/database-testing", "https://laravel.com/framework/docs/13.x/testing"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Laravel: entender quando RefreshDatabase usa transação

## Em uma frase
`RefreshDatabase` limpa o estado entre testes e, se o schema já estiver atualizado, executa o teste em transação sem migrar novamente.

## Por que importa
O mecanismo acelera isolamento comum, mas não significa que cada teste refaça migrations nem que qualquer efeito fora do banco seja revertido.

## Como funciona
Use o trait na classe de Feature tests e escolha `DatabaseMigrations` ou `DatabaseTruncation` quando a semântica completa de reset for realmente necessária.

## Exemplo
Um teste cria um usuário via factory dentro da transação e não deixa esse registro disponível para o próximo teste.

## Limites e trade-offs
Migrations e truncation podem custar mais, e conexões externas não participam automaticamente da transação do banco de teste.

## Como verificar
Verifique migrations, driver e estado persistido após o caso; teste hooks de commit separadamente quando forem parte do contrato.

## Conexões
- [[laravel-testing-environment-boundary]] — Veja também: Laravel: isolar configuração do ambiente testing.
- [[laravel-http-test-internal-request]] — Veja também: Laravel: testar rota com request simulado internamente.

## Fontes
- [Laravel 13 — Database testing](https://laravel.com/framework/docs/13.x/database-testing) — refresh de banco, factories, assertions de persistência e isolamento; consultado em 2026-10-02.
- [Laravel 13 — Testing](https://laravel.com/framework/docs/13.x/testing) — tipos de testes, ambiente testing, banco, helpers e execução paralela; consultado em 2026-10-02.
