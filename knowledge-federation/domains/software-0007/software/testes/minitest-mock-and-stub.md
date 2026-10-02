---
id: software.testes.tranche15.000885
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://docs.seattlerb.org/minitest/Minitest/Mock.html", "https://docs.seattlerb.org/minitest/Minitest/Test.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Minitest: isolar colaboradores com mock e stub

## Em uma frase
`Minitest::Mock` registra expectativas e verifica chamadas ao final do teste, enquanto o método `stub` substitui um objeto por um retorno controlado durante o bloco.

## Por que importa
Substituir colaboradores reais reduz dependências lentas, mas expectativas permissivas demais deixam o teste passar mesmo quando a integração está errada.

## Como funciona
Declare apenas as mensagens esperadas, verifique argumentos relevantes e prefira o bloco de stub para que a substituição seja revertida automaticamente.

## Exemplo
`servico = Minitest::Mock.new; servico.expect(:cobrar, true, [100]); servico.cobrar(100); servico.verify` falha se a chamada esperada não ocorrer.

## Limites e trade-offs
Mocks verificam contrato de chamada, não o comportamento interno do colaborador real; stub silencioso em excesso pode esconder que o objeto não foi procurado.

## Como verificar
Faça a verificação após uma chamada ausente e confirme a falha, garantindo que as expectativas não estejam sendo apenas declaradas sem verificação.

## Conexões
- [[minitest-spec-dsl]] — Veja também: Minitest: usar a DSL de spec.
- [[minitest-parallelize-me]] — Veja também: Minitest: paralelizar testes com segurança.

## Fontes
- [Minitest — Mock](https://docs.seattlerb.org/minitest/Minitest/Mock.html) — mocks com expectativas, verificação de chamadas e stubs temporários; consultado em 2026-10-02.
- [Minitest — Test](https://docs.seattlerb.org/minitest/Minitest/Test.html) — classes de teste, ciclos de vida, ordem aleatória e paralelização; consultado em 2026-10-02.
