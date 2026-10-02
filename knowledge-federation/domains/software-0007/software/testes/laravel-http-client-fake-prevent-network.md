---
id: software.testes.tranche14.000835
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
fontes: ["https://laravel.com/framework/docs/13.x/http-client#testing", "https://laravel.com/framework/docs/13.x/testing"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Laravel: impedir tráfego HTTP real com Http::fake

## Em uma frase
`Http::fake` substitui respostas de saída do HTTP client Laravel e pode evitar que teste faça requests para serviços externos.

## Por que importa
Uma dependência de rede fora do processo cria instabilidade, custo, exposição de dados e resultados não determinísticos.

## Como funciona
Defina fakes por padrão e ative prevenção de requests não registrados quando a suite exigir que todo tráfego externo seja explicitamente configurado.

## Exemplo
Uma integração de cobrança recebe resposta de timeout simulada e o caso valida política de retry sem acessar o gateway real.

## Limites e trade-offs
Fake de facade não intercepta automaticamente todos os clientes HTTP de terceiros usados pela aplicação.

## Como verificar
Faça uma assertion de request enviado e configure falha para destinos não previstos, revisando cada biblioteca de rede do sistema.

## Conexões
- [[laravel-json-path-assertions]] — Veja também: Laravel: validar contrato JSON por caminho sem comparar payload inteiro.
- [[laravel-event-fake-scope]] — Veja também: Laravel: usar Event fake sem ocultar listener necessário.

## Fontes
- [Laravel 13 — HTTP Client testing](https://laravel.com/framework/docs/13.x/http-client#testing) — fakes de respostas HTTP, inspeção de requests e prevenção de tráfego real; consultado em 2026-10-02.
- [Laravel 13 — Testing](https://laravel.com/framework/docs/13.x/testing) — tipos de testes, ambiente testing, banco, helpers e execução paralela; consultado em 2026-10-02.
