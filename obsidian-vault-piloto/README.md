# Obsidian Vault Piloto — Engenharia de Software, Arquitetura e Jogos 2D

Este vault foi montado para gerar um **Graph View automático** com três constelações principais:

1. **Engenharia de Software** — práticas de evolução, qualidade e entrega.
2. **Arquitetura de Software** — decisões estruturais, padrões e fronteiras.
3. **Desenvolvimento de Jogos 2D** — gameplay, renderização, estado, produção e UX.

O desenho do grafo vem da estrutura de links:

- `00-Mapas/` contém MOCs, que funcionam como hubs.
- `01-Notas/` contém fichas estruturadas e atômicas.
- notas com tag `ponte` conectam clusters diferentes.
- `.obsidian/graph.json` configura cores por grupos de tags.

## Como usar

1. Descompacte `obsidian-vault-piloto.zip` ou copie a pasta `obsidian-vault-piloto`.
2. No Obsidian, escolha **Open folder as vault** e selecione essa pasta.
3. Abra o Graph View.
4. Ative filtros por grupos, se necessário, e use as tags:
   - `tag:#moc`
   - `tag:#software`
   - `tag:#arquitetura`
   - `tag:#jogos2d`
   - `tag:#ponte`

## Como continuar a automação

Para cada nova rodada, forneça:

```text
Tema: <tema central>
Escopo: <o que entra e o que fica fora>
Profundidade: semente | intermediário | avançado
Quantidade: <número de notas>
Objetivo visual: cluster novo | expandir cluster | criar ponte entre clusters
Formato: ficha estruturada
```

Exemplo:

```text
Tema: combate 2D para metroidvania
Escopo: input buffering, hitboxes, inimigos básicos, feedback e balanceamento inicial
Profundidade: intermediário
Quantidade: 20 notas
Objetivo visual: expandir cluster jogos2d e criar ponte com arquitetura
Formato: ficha estruturada
```
