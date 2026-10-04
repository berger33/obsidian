---
id: software.criacao_ia.tranche02.000144
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-02.md"
fontes: ["https://docs.unity3d.com/Packages/com.unity.animation.rigging@1.3/manual/index.html", "https://docs.unity3d.com/Packages/com.unity.animation.rigging@1.3/manual/constraints/TwoBoneIKConstraint.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Unity: suavizar movimento de armas e acessórios com Damp Transform

## Em uma frase
A restrição Damp Transform aplica amortecimento inercial em objetos acoplados ao personagem durante movimentos rápidos.

## Por que importa
Acessórios como capas, coldres e armas longas parecem blocos rígidos e sem vida se fixados diretamente a ossos sem inércia física.

## Como funciona
Insira a restrição `DampTransform` no osso do acessório, configurando os fatores de amortecimento posicional e rotacional para criar um atraso de movimento convincente.

## Exemplo
```csharp
// Exemplo de ajuste de amortecimento inercial no componente DampTransform
// Os parametros damping e rotDamping controlam a velocidade de recuperacao
dampTransformConstraint.data.damping = 0.35f;
```

## Limites e trade-offs
Valores de amortecimento muito altos fazem o acessório se deslocar excessivamente do corpo durante corridas, atravessando a malha do personagem.

## Como verificar
Verifique a animação em velocidades variadas de corrida e giros rápidos para garantir que o acessório reaja sem atravessar a geometria do corpo.

## Conexões
- [[unity-animation-rigging-orientar-olhar-com-multi-aim]] — Veja também: Unity: orientar cabeça e olhar com Multi-Aim Constraint.
- [[unity-utility-ai-avaliar-decisoes-com-curvas]] — Veja também: Unity: avaliar decisões de NPCs com curvas de resposta em Utility AI.
- [[unity-animation-rigging-montar-rigbuilder]] — Conexão temática direta com unity-animation-rigging-montar-rigbuilder.
- [[blender-separar-movimento-in-place-e-root-motion]] — Conexão temática direta com blender-separar-movimento-in-place-e-root-motion.
- [[assets-ia-otimizar-compressao-bc7-e-astc-em-vram]] — Conexão temática direta com assets-ia-otimizar-compressao-bc7-e-astc-em-vram.

## Fontes
- [Unity Animation Rigging Package Manual](https://docs.unity3d.com/Packages/com.unity.animation.rigging@1.3/manual/index.html) — Documentação oficial do componente rigbuilder, restrições procedurais twoboneik, multi-aim e damptransform. Consulta: 2026-10-04.
- [Unity Animation Rigging — TwoBoneIKConstraint](https://docs.unity3d.com/Packages/com.unity.animation.rigging@1.3/manual/constraints/TwoBoneIKConstraint.html) — Referência técnica detalhando parâmetros de ik, targets polares e ajuste dinâmico em superfícies. Consulta: 2026-10-04.
