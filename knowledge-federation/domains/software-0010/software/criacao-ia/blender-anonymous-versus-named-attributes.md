---
id: software.criacao_ia.tranche03.000243
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-03.md"
fontes: ["https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attributes_reference.html", "https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Blender Geometry Nodes: escolher atributo anônimo ou nomeado

## Em uma frase
Atributos anônimos circulam por sockets de Geometry Nodes sem nome; atributos nomeados atendem usos em áreas do Blender como shaders e UV mapping.

## Por que importa
Nomear todos os valores temporários aumenta risco de colisão e escrita acidental sobre atributos que já existem no objeto. Por outro lado, dados que precisam cruzar um limite para shading ou outra ferramenta podem exigir interface nomeada e persistência explícita.

## Como funciona
Use Capture Attribute para dados intermediários locais que serão consumidos por links downstream. Use Store Named Attribute e Named Attribute quando outra parte do Blender precisar consultar o identificador pelo nome. A disponibilidade de atributo anônimo depende da geometria ligada; ele não pode ser conectado diretamente a uma geometry independente de outra origem.

## Exemplo
Uma graph calcula peso transitório para selecionar pontos e guarda o field por link anônimo, evitando uma string compartilhada. Se o shader deve ler máscara de desgaste, armazene essa máscara com nome definido e confirme que o domínio e tipo correspondem ao material.

## Limites e trade-offs
Atributos anônimos podem ser interpolados quando a geometria muda, com exceções por operação, e simulation zones exigem armazenamento explícito no estado. Um nome explícito não garante que o atributo sobreviva a cada nó nem que tenha tipo esperado.

## Como verificar
Use o Named Attributes overlay para procurar colisões e Spreadsheet para confirmar nome, tipo e domain. Teste junção de geometrias e nós que criam geometry nova para observar se o atributo continua disponível.

## Conexões
- [[blender-capture-attribute-antes-de-conversao]] — Blender: capturar fields antes de uma conversão de geometria.
- [[blender-attributes-domain-conversoes-implicitas]] — Blender Geometry Nodes: auditar domínio e conversão de atributos.

## Fontes
- [Blender 5.2 LTS — Attributes](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attributes_reference.html) — define atributos anônimos/nomeados e limites de transferência entre geometrias Consulta: 2026-10-04.
- [Blender 5.2 LTS — Capture Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) — compara captura temporária anônima com Store/Named Attribute Consulta: 2026-10-04.
