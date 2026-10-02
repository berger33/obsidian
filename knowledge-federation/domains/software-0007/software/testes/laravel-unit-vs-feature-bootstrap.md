---
id: software.testes.tranche14.000830
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
fontes: ["https://laravel.com/framework/docs/13.x/testing", "https://laravel.com/framework/docs/13.x/http-tests"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Laravel: escolher Unit ou Feature pelo bootstrap necessário

## Em uma frase
Testes Unit não iniciam a aplicação Laravel e por isso não acessam automaticamente banco ou serviços do framework; Feature tests podem atravessar objetos e requests HTTP.

## Por que importa
Escolher a fronteira pelo comportamento testado evita tanto bootstrap caro para uma função pura quanto falsa expectativa de infraestrutura em teste unitário.

## Como funciona
Use classe PHPUnit sem base da aplicação para lógica independente e `Tests\TestCase` para helpers de framework e comportamento integrado.

## Exemplo
Uma função de normalização pura fica em Unit, enquanto autorização de rota e resposta JSON entram em Feature.

## Limites e trade-offs
Herança de classe e convenções do projeto podem mudar o bootstrap, então confirme a base real configurada no repositório.

## Como verificar
Execute o mesmo caso com a base pretendida e verifique se a aplicação, banco ou serviços foram de fato inicializados.

## Conexões
- [[laravel-testing-environment-boundary]] — Veja também: Laravel: isolar configuração do ambiente testing.

## Fontes
- [Laravel 13 — Testing](https://laravel.com/framework/docs/13.x/testing) — tipos de testes, ambiente testing, banco, helpers e execução paralela; consultado em 2026-10-02.
- [Laravel 13 — HTTP tests](https://laravel.com/framework/docs/13.x/http-tests) — requests internos, respostas JSON e assertions sobre aplicações HTTP; consultado em 2026-10-02.
