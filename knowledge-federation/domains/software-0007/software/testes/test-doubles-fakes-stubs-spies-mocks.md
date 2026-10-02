---
id: software.testes.test-doubles.000001
tipo: conceito
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-01
validade: estavel
status: candidata
revisao_humana: aprovada
revisor: usuario-da-sessao
data_revisao_humana: 2026-10-02
fontes: ["https://martinfowler.com/bliki/TestDouble.html", "https://martinfowler.com/articles/mocksArentStubs.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: [Test double, Mock, Stub, Fake, Spy, Dummy]
lote: software-testes-2000-0001
---

# Test doubles: dummies, fakes, stubs, spies e mocks

## Em uma frase
Test double é um substituto de um colaborador real usado por um teste; os termos dummy, fake, stub, spy e mock descrevem papéis diferentes desse substituto.

## Por que importa
Dependências reais podem tornar um teste lento, imprevisível ou capaz de produzir efeitos externos, como enviar e-mail. Um substituto controlado ajuda a isolar o comportamento sob teste, mas a escolha errada pode esconder falhas de integração ou acoplar a suíte a detalhes internos. Usar “mock” como nome genérico para qualquer objeto falso dificulta entender o que cada teste realmente verifica.

## Como funciona
Um dummy é fornecido para preencher um parâmetro sem ser usado. Um fake tem uma implementação funcional simplificada, como um repositório em memória. Um stub retorna respostas preparadas para chamadas específicas. Um spy registra como foi chamado e permite examinar essas interações depois. Um mock é configurado com expectativas de chamadas e as verifica durante o teste. Fowler também distingue verificação de estado — observar o resultado no objeto — de verificação de comportamento — conferir interações esperadas.

## Exemplo
Ao testar um serviço de pedidos, um fake de repositório pode manter pedidos em memória para verificar o estado final. Um stub de gateway de pagamento pode devolver uma recusa previsível. Um mock pode ser apropriado quando o efeito principal esperado é chamar um serviço externo com uma mensagem específica; não é necessário transformar toda colaboração em mock.

## Limites e trade-offs
Doubles não provam que a dependência real obedece ao contrato configurado no teste. Mocks excessivos podem fazer testes falharem quando a implementação muda sem alterar o comportamento visível. Fakes podem divergir do sistema real, sobretudo em transações e concorrência. Use testes de integração ou contrato onde seja importante verificar a fronteira real.

## Como verificar
Para cada double, identifique se o teste verifica estado, resposta preparada, chamada registrada ou expectativa de interação. Confira que o teste falharia diante do defeito relevante e que um teste separado cobre a integração que o double substitui. Evite expectativas sobre chamadas internas que não fazem parte do contrato do componente.

## Conexões
- [[testes-hermeticos-dependencias]] — doubles podem substituir dependências não declaradas, mas não são a única forma de tornar testes herméticos.
- [[fixtures-pytest-ciclo-vida-escopos]] — fixtures podem construir doubles e controlar sua duração.
- [[mutation-testing-eficacia-testes]] — mutação ajuda a investigar se as verificações realmente detectam mudanças de comportamento.

## Fontes
- [Martin Fowler — Test Double](https://martinfowler.com/bliki/TestDouble.html) — vocabulário para dummy, fake, stub, spy e mock; acesso em 2026-10-01.
- [Martin Fowler — Mocks Aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html) — estado versus comportamento e estilos de verificação; acesso em 2026-10-01.
