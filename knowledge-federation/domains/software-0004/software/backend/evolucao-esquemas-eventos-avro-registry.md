---
id: software.backend.evolucao-esquemas-eventos.000001
tipo: tecnica
dominio: software
subdominio: backend
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: aprovada
revisor: usuario-da-sessao
data_revisao_humana: 2026-10-02
fontes: ["https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html", "https://avro.apache.org/docs/1.11.1/specification/"]
tags: [dominio/software, subdominio/backend, qualidade/candidata]
aliases: [Evolução de esquema, Schema Registry compatibility, Compatibilidade Avro]
lote: software-dados-distribuidos-0004
---

# Evolução de esquemas para eventos distribuídos

## Em uma frase
Evoluir o esquema de um evento exige definir quais versões de produtores e consumidores poderão coexistir e validar essa compatibilidade antes de publicar dados novos.

## Por que importa
Eventos podem permanecer em tópicos e ser lidos muito depois de terem sido produzidos. Uma alteração que funciona com o produtor atual ainda pode quebrar um consumidor antigo ou uma reconstrução histórica. Compatibilidade é uma relação entre versões e direções de leitura, não apenas a validade sintática de um documento.

## Como funciona
No Schema Registry da Confluent, os modos backward, forward e full representam relações diferentes entre leitores e dados antigos/novos; modos transitive comparam a nova versão a todas as versões anteriores, enquanto modos não transitive comparam com a versão imediatamente anterior. A regra padrão do produto é backward. Os detalhes dependem do formato e de como campos foram declarados. No Avro, valores default participam da resolução quando o esquema do leitor encontra um campo ausente nos dados do escritor; o default não torna o campo opcional durante a codificação. O modo de compatibilidade também influencia a ordem segura de atualização de produtores e consumidores.

## Exemplo
Se consumidores novos precisam ler mensagens antigas, uma mudança pode precisar ser backward-compatible. Uma equipe pode adicionar um campo com default e validar a nova definição contra as versões registradas antes de implantá-la. Se consumidores antigos também precisarem interpretar eventos produzidos pelo escritor novo, avalie compatibilidade forward ou full conforme o formato e o contrato.

## Limites e trade-offs
Os rótulos e regras do Schema Registry são específicos do produto e variam entre Avro, Protobuf e JSON Schema. Compatibilidade estrutural não garante que a semântica de negócio permaneça igual; mudar o significado de um campo pode quebrar consumidores sem alterar seu tipo. A política escolhida também pode ignorar versões antigas se não for transitive. Não trate a aprovação do registry como prova de que todas as aplicações processam o evento corretamente.

## Como verificar
Teste a matriz escritor/leitor entre versões suportadas, incluindo mensagens históricas e consumers em processo de rollout. Execute a verificação de compatibilidade na CI antes de registrar o novo schema e valide valores default, campos removidos e mudanças semânticas com testes de contrato. Documente o modo, o formato e a sequência de implantação que a equipe suporta.

## Conexões
- [[outbox-transacional-publicacao-eventos]] — o evento publicado pela outbox precisa de payload compatível com consumidores ao longo do tempo.
- [[entrega-kafka-at-least-once-consumidor-idempotente]] — replays podem fazer consumidores antigos encontrarem esquemas anteriores.
- [[migracoes-expand-contract]] — deploy gradual de produtores, consumidores e schemas se beneficia de mudanças compatíveis.

## Fontes
- [Confluent — Schema Evolution and Compatibility](https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html) — modos de compatibilidade e implicações de rollout no Schema Registry; acesso em 2026-10-01.
- [Apache Avro — Specification 1.11.1](https://avro.apache.org/docs/1.11.1/specification/) — defaults e resolução entre esquemas escritor/leitor; acesso em 2026-10-01.
